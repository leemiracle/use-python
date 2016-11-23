import PIL.Image
import tempfile
import base64
import os
import io
import barcode
from barcode.writer import ImageWriter


def generate_barcode_binary(data):
    ean = barcode.get('ean13', data, writer=ImageWriter())
    img = ean.render()
    tmp = tempfile.mktemp()
    img.save(tmp, 'GIF')
    with open(tmp, 'rb')as f:
        binary = f.read()
    os.remove(tmp)
    return binary

