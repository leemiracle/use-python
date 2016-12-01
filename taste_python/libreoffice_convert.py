"""
参考aeroo_docs和pyodconverter项目
处理流程：
1.$ soffice "-accept=socket,port=2002;urp;"

2.get the uno component context from the PyUNO runtime
localContext = uno.getComponentContext()

3.create the UnoUrlResolver
resolver = localContext.ServiceManager.createInstanceWithContext(
				"com.sun.star.bridge.UnoUrlResolver", localContext )

4.connect to the running office
ctx = resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )
smgr = ctx.ServiceManager

5.get the central desktop object
desktop = smgr.createInstanceWithContext( "com.sun.star.frame.Desktop",ctx)

6.access the current writer document/文档
model = desktop.getCurrentComponent()

"""

#
# PyODConverter (Python OpenDocument Converter) v1.2 - 2012-03-10
#
# This script converts a document from one office format to another by
# connecting to an OpenOffice.org instance via Python-UNO bridge.
#
# Copyright (C) 2008-2012 Mirko Nasato
# Licensed under the GNU LGPL v2.1 - http://www.gnu.org/licenses/lgpl-2.1.html
# - or any later version.
#
DEFAULT_OPENOFFICE_PORT = 8100
DEFAULT_OPENOFFICE_HOST = "localhost"

import uno
import unohelper

from os.path import abspath, isfile, splitext
from io import BytesIO
import sys
import traceback

from com.sun.star.io import XOutputStream
from com.sun.star.beans import PropertyValue, UnknownPropertyException
from com.sun.star.task import ErrorCodeIOException
from com.sun.star.connection import NoConnectException, ConnectionSetupException
from com.sun.star.lang import IllegalArgumentException, DisposedException
from com.sun.star.document.UpdateDocMode import QUIET_UPDATE
from com.sun.star.document.MacroExecMode import NEVER_EXECUTE

FAMILY_TEXT = "Text"
FAMILY_WEB = "Web"
FAMILY_SPREADSHEET = "Spreadsheet"
FAMILY_PRESENTATION = "Presentation"
FAMILY_DRAWING = "Drawing"

# ---------------------#
# Configuration Start #
# ---------------------#

# see http://wiki.services.openoffice.org/wiki/Framework/Article/Filter

# most formats are auto-detected; only those requiring options are defined here
IMPORT_FILTER_MAP = {
    "txt": {
        "FilterName": "Text (encoded)",
        "FilterOptions": "utf8"
    },
    "csv": {
        "FilterName": "Text - txt - csv (StarCalc)",
        "FilterOptions": "44,34,0"
    }
}

EXPORT_FILTER_MAP = {
    "pdf": {
        FAMILY_TEXT: {"FilterName": "writer_pdf_Export"},
        FAMILY_WEB: {"FilterName": "writer_web_pdf_Export"},
        FAMILY_SPREADSHEET: {"FilterName": "calc_pdf_Export"},
        FAMILY_PRESENTATION: {"FilterName": "impress_pdf_Export"},
        FAMILY_DRAWING: {"FilterName": "draw_pdf_Export"}
    },
    "html": {
        FAMILY_TEXT: {"FilterName": "HTML (StarWriter)"},
        FAMILY_SPREADSHEET: {"FilterName": "HTML (StarCalc)"},
        FAMILY_PRESENTATION: {"FilterName": "impress_html_Export"}
    },
    "odt": {
        FAMILY_TEXT: {"FilterName": "writer8"},
        FAMILY_WEB: {"FilterName": "writerweb8_writer"}
    },
    "doc": {
        FAMILY_TEXT: {"FilterName": "MS Word 97"}
    },
    "rtf": {
        FAMILY_TEXT: {"FilterName": "Rich Text Format"}
    },
    "txt": {
        FAMILY_TEXT: {
            "FilterName": "Text",
            "FilterOptions": "utf8"
        }
    },
    "ods": {
        FAMILY_SPREADSHEET: {"FilterName": "calc8"}
    },
    "xls": {
        FAMILY_SPREADSHEET: {"FilterName": "MS Excel 97"}
    },
    "csv": {
        FAMILY_SPREADSHEET: {
            "FilterName": "Text - txt - csv (StarCalc)",
            "FilterOptions": "44,34,0"
        }
    },
    "odp": {
        FAMILY_PRESENTATION: {"FilterName": "impress8"}
    },
    "ppt": {
        FAMILY_PRESENTATION: {"FilterName": "MS PowerPoint 97"}
    },
    "swf": {
        FAMILY_DRAWING: {"FilterName": "draw_flash_Export"},
        FAMILY_PRESENTATION: {"FilterName": "impress_flash_Export"}
    }
}

PAGE_STYLE_OVERRIDE_PROPERTIES = {
    FAMILY_SPREADSHEET: {
        # --- Scale options: uncomment 1 of the 3 ---
        # a) 'Reduce / enlarge printout': 'Scaling factor'
        "PageScale": 100,
        # b) 'Fit print range(s) to width / height': 'Width in pages' and 'Height in pages'
        # "ScaleToPagesX": 1, "ScaleToPagesY": 1000,
        # c) 'Fit print range(s) on number of pages': 'Fit print range(s) on number of pages'
        # "ScaleToPages": 1,
        "PrintGrid": False
    }
}


# -------------------#
# Configuration End #
# -------------------#

class DocumentConversionException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class OutputStreamWrapper(unohelper.Base, XOutputStream):
    """ Minimal Implementation of XOutputStream """

    def __init__(self, debug=True):
        self.debug = debug
        self.data = BytesIO()
        self.position = 0
        if self.debug:
            sys.stderr.write("__init__ OutputStreamWrapper.\n")

    def writeBytes(self, bytes):
        if self.debug:
            sys.stderr.write("writeBytes %i bytes.\n" % len(bytes.value))
        self.data.write(bytes.value)
        self.position += len(bytes.value)

    def close(self):
        if self.debug:
            sys.stderr.write("Closing output. %i bytes written.\n" % self.position)
        self.data.close()

    def flush(self):
        if self.debug:
            sys.stderr.write("Flushing output.\n")
        pass

    def closeOutput(self):
        if self.debug:
            sys.stderr.write("Closing output.\n")
        pass


class DocumentConverter:
    def __init__(self, host=DEFAULT_OPENOFFICE_HOST,port=DEFAULT_OPENOFFICE_PORT):
        # UNO component context
        self.localContext = uno.getComponentContext()
        self.serviceManager = self.localContext.ServiceManager
        # UnoUrlResolver
        self.resolver = self.localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver",
                                                                              self.localContext)
        try:
            self.context = self.resolver.resolve("uno:socket,host=%s,port=%s;urp;StarOffice.ComponentContext" % (host, port))
        except NoConnectException:
            raise(DocumentConversionException, "failed to connect to OpenOffice.org on port %s" % port)
        self.desktop = self.context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", self.context)

    def convert_by_path(self, inputFile, outputFile):

        inputUrl = self._toFileUrl(inputFile)
        outputUrl = self._toFileUrl(outputFile)

        loadProperties = {"Hidden": True}
        inputExt = self._getFileExt(inputFile)
        if inputExt in IMPORT_FILTER_MAP:
            loadProperties.update(IMPORT_FILTER_MAP[inputExt])

        document = self.desktop.loadComponentFromURL(inputUrl, "_blank", 0, self._toProperties(loadProperties))
        try:
            document.refresh()
        except AttributeError:
            pass

        family = self._detectFamily(document)
        self._overridePageStyleProperties(document, family)

        outputExt = self._getFileExt(outputFile)
        storeProperties = self._getStoreProperties(document, outputExt)

        try:
            document.storeToURL(outputUrl, self._toProperties(storeProperties))
        finally:
            document.close(True)

    def _overridePageStyleProperties(self, document, family):
        if family in PAGE_STYLE_OVERRIDE_PROPERTIES:
            properties = PAGE_STYLE_OVERRIDE_PROPERTIES[family]
            pageStyles = document.getStyleFamilies().getByName('PageStyles')
            for styleName in pageStyles.getElementNames():
                pageStyle = pageStyles.getByName(styleName)
                for name, value in properties.items():
                    pageStyle.setPropertyValue(name, value)

    def _getStoreProperties(self, document, outputExt):
        family = self._detectFamily(document)
        try:
            propertiesByFamily = EXPORT_FILTER_MAP[outputExt]
        except KeyError:
            raise(DocumentConversionException, "unknown output format: '%s'" % outputExt)
        try:
            return propertiesByFamily[family]
        except KeyError:
            raise(DocumentConversionException, "unsupported conversion: from '%s' to '%s'" % (family, outputExt))

    def _detectFamily(self, document):
        if document.supportsService("com.sun.star.text.WebDocument"):
            return FAMILY_WEB
        if document.supportsService("com.sun.star.text.GenericTextDocument"):
            # must be TextDocument or GlobalDocument
            return FAMILY_TEXT
        if document.supportsService("com.sun.star.sheet.SpreadsheetDocument"):
            return FAMILY_SPREADSHEET
        if document.supportsService("com.sun.star.presentation.PresentationDocument"):
            return FAMILY_PRESENTATION
        if document.supportsService("com.sun.star.drawing.DrawingDocument"):
            return FAMILY_DRAWING
        raise(DocumentConversionException, "unknown document family: %s" % document)

    def _getFileExt(self, path):
        ext = splitext(path)[1]
        if ext is not None:
            return ext[1:].lower()

    def _toFileUrl(self, path):
        return uno.systemPathToFileUrl(abspath(path))

    def _toProperties(self, **args):
        props = []
        for key in args:
            prop = PropertyValue()
            prop.Name = key
            prop.Value = args[key]
            props.append(prop)
        return tuple(props)


    def putDocument(self, data, filter_name=False, read_only=False):
        """
        Uploads document to office service
        """
        inputStream = self._initStream(data)
        properties = {'InputStream': inputStream}
        properties.update({'Hidden': True})
        properties.update({'UpdateDocMode': QUIET_UPDATE})
        properties.update({'ReadOnly': read_only})
        properties.update({'MacroExecutionMode': NEVER_EXECUTE})

        # TODO Minor performance improvement by supplying MediaType property
        # properties.update({'MediaType':'application/vnd.oasis.opendocument.text'})

        if filter_name:
            properties.update({'FilterName': filter_name})
        props = self._toProperties(**properties)
        try:
            self.document = self.desktop.loadComponentFromURL('private:stream', '_blank', 0, props)
        except DisposedException as e:
            #   When office unexpectedly crashed or has been restarted, we know
            # nothing about it, that is why we need to create new desktop or
            # even try to completely reconnect to new office socket. Then give
            # it another try.
            self.putDocument(data, filter_name=filter_name, read_only=read_only)
        except Exception as e:
            exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
            traceback.print_exception(exceptionType, exceptionValue,
                                      exceptionTraceback, limit=2, file=sys.stdout)
        inputStream.closeInput()

    def saveByStream(self, filter_name="writer_pdf_Export"):
        """
        Downloads document from office service
        """
        self._updateDocument()
        outputStream = OutputStreamWrapper(False)
        properties = {"OutputStream": outputStream}
        properties.update({"FilterName": filter_name})
        if filter_name == 'Text - txt - csv (StarCalc)':
            properties.update({"FilterOptions": "44,34,0"})
        props = self._toProperties(**properties)
        try:
            # url = uno.systemPathToFileUrl(path) #when storing to filesystem
            self.document.storeToURL('private:stream', props)
        except Exception as exception:
            exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
            traceback.print_exception(exceptionType, exceptionValue,
                                      exceptionTraceback, limit=2, file=sys.stdout)
        openDocumentBytes = outputStream.data.getvalue()
        outputStream.close()
        return openDocumentBytes

    def _updateDocument(self):
        try:
            self.document.updateLinks()
        except AttributeError:
            # if document doesn't support XLinkUpdate interface
            pass
        try:
            self.document.refresh()
            indexes = self.document.getDocumentIndexes()
        except AttributeError:
            # ods document does not support refresh
            pass
        else:
            for inc in range(0, indexes.getCount()):
                indexes.getByIndex(inc).update()

    def _initStream(self, data):
        streamvector = "com.sun.star.io.SequenceInputStream"
        subStream = self.serviceManager.createInstanceWithContext(streamvector, self.localContext)
        subStream.initialize((uno.ByteSequence(data),))
        return subStream


if __name__ == "__main__":
    from sys import argv, exit

    if len(argv) < 3:
        print("USAGE: python %s <input-file> <output-file>" % argv[0])
        exit(255)
    if not isfile(argv[1]):
        print("no such input file: %s" % argv[1])
        exit(1)

    try:
        converter = DocumentConverter()
        converter.convert_by_path(argv[1], argv[2])
    except DocumentConversionException:
        print("ERROR! " + str(DocumentConversionException))
        exit(1)
    except ErrorCodeIOException:
        print("ERROR! ErrorCodeIOException %d" % ErrorCodeIOException.ErrCode)
        exit(1)
