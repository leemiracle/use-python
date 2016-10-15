import time

import datetime


def test_convert_unicode_ascii():
    # 将编码int转换字符
    chr(97)

    # 将字符转换为unicode编码int
    ord('a')


def delete_special_character(string):
    """
    删除字符串中特殊字符
    :param string:
    :return:
    """
    return ''.join(e for e in string if e.isalnum())


def convert_date_to_timestamp(string):
    """
    将 日/月/年 转 时间戳
    :param string:
    :return:
    """
    return time.mktime(datetime.datetime.strptime(string.strip(), "%d/%m/%Y").timetuple())


def test_re():
    import re
    # 验证 字符是否在给定的unicode编码表的编码范围内(ascii英文字符编码和unicode编码，编号一致)通过,字符数量为1-20个
    re_pattern_match = re.compile(r'^[\u0021-\u007E]{1,20}$')
    test_re_success = re_pattern_match.match('!@#$%~^&*()_+|]')
    assert test_re_success is not None
    test_re_fail = re_pattern_match.match('！中国')
    assert test_re_fail is None

if __name__ == '__main__':
    test_convert_unicode_ascii()
    test_re()
