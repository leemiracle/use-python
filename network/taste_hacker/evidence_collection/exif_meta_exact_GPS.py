"""
元数据

理解 Exif 元数据:
    Exif 格式就是在 JPEG 格式头部插入了数码照片的信息,包括拍摄时的光圈、快门、白平衡、ISO、焦距、日期时间等各种和拍摄条件以及相机品牌、型号、
色彩编码、拍摄时录制的声音以及全球定位系统(GPS)、缩略图等。简单地说,Exif=JPEG+拍摄参数。
"""

# 使用 PyPDF 解析 PDF 元数据
import pyPdf
from pyPdf import PdfFileReader

def printMeta(fileName):
    pdfFile = PdfFileReader(file(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print('[*] PDF MetaData For: ' + str(fileName))
    for metaItem in docInfo:
        print('[+] ' + metaItem + ':' + docInfo[metaItem])


# 理解 Exif 元数据
#   Phil Harvey 编写了一个实用的工具名叫 exiftool(从 http://www.sno.phy.queensu.ca/~phil/exiftool/可获得)能解析这
# 些参数。检查所有的 Exif 参数可能会返回几页的信息,所以我们只检查部分需要的参数信息。

# BeautifulSoup 允许我们快速的解析 HTML 和 XML 文档

# 使用 Python 图像库 PIL 来处理文件,
from PIL import Image
from PIL.ExifTags import TAGS

def testForExif(imgFileName):
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()
        if info:
    for (tag, value) in info.items():
        decoded = TAGS.get(tag, tag)
        exifData[decoded] = value
        exifGPS = exifData['GPSInfo']
        if exifGPS:
            print('[*] ' + imgFileName + ' contains GPS MetaData')
    except:
        pass
