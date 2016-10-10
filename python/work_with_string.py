
# 删除字符串中特殊字符
def delete_special_character(string):
    return ''.join(e for e in string if e.isalnum())