# coding=Utf-8
"""
用字典暴力破解ZIP压缩文件密码
"""

import zipfile
import threading

def extractFile(zFile, password):
    """zFile用于对zip文件进行操作"""
    try:
        # 用密码试提取文件
        zFile.extractall(pwd=password)
        print("Found Passwd : ", password)
        return password
    except:
        pass


def main():
    """threading为多线程, """
    zFile = zipfile.ZipFile('unzip.zip')
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        t = threading.Thread(target=extractFile, args=(zFile, password))
        t.start()
        """
        guess = extractFile(zFile, password)
        if guess:
            print('Password = ', password)
            return
        else:
            print("can't find password")
            return
        """




if __name__ == '__main__':
    test_argparse_interact_with_comandline()
    # main()

