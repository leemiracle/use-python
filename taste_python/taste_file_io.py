from os.path import join, dirname
import base64
from io import BytesIO
import imghdr


def test_file_base64_convert():
    with open(join(dirname(__file__), '559887717.png'), 'rb') as f:
        data = f.read()
        # binary转base64
        string_base64 = base64.b64encode(data)
        # base64转binary
        binary = base64.b64decode(string_base64)
        # binary 转文件
        bytes_file = BytesIO(binary)


def test_detect_file_type():
        # 获取image文件的格式
        with open(join(dirname(__file__), '559887717.png'), 'rb') as f:
            file_extend = imghdr.what(f)
        return file_extend
