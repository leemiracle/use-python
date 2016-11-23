"""
生成二维码
"""

from pyqrcode import QRCode
import base64
from PIL import Image
import tempfile
import io
import os


# url.png('code.png')


def generate_qrcode_binary(qrcode):
    """"""

    binary = base64.decodebytes(qrcode.png_as_base64_str().encode('ascii'))
    img = Image.open(io.BytesIO(binary))
    tmp = tempfile.mktemp()
    # 生成格式为png的二维码,放入pdf中进行渲染时异常，故转换为gif格式
    img.save(tmp, 'GIF')
    with open(tmp, 'rb')as f:
        binary = f.read()
    os.remove(tmp)
    return binary
data = 'http://uca.edu'
qrcode = QRCode(data, mode='binary', encoding='utf-8', error='H')
binary = generate_qrcode_binary('http://uca.edu')
print(qrcode.data)

