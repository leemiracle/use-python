
# 将编码int转换字符
chr()

# 将字符转换为unicode编码int
ord()


def delete_special_character(string):
    """
    删除字符串中特殊字符
    :param string:
    :return:
    """
    return ''.join(e for e in string if e.isalnum())