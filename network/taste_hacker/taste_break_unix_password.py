"""
(暴力破解)UNIX的密码,需要输入字典文件和UNIX的密码文件
现代unix系统存储在/etc/shadow 文件中,提供了个更安全的希散列算法 SHA-512 算法,
Python 的标准库中 hashlib 模块提供了此算法
"""

import crypt

def testPass(cryptPass):
    """破解unix系统密码"""
    # 假设盐只有两位
    salt = cryptPass[0:2]
    dictfile = open('dictionary.txt', 'r') #打开字典文件
    for word in dictfile.readlines():
        word = word.strip('\n') #保留原始的字符,不去空格
        cryptWord = crypt.crypt(word, salt)
        if cryptPass == cryptWord:
            print('Found passed : ', word)
            return
    print('Password not found !')
    return


def main():
    passfile = open('passwords.txt', 'r') #读取密码文件
    for line in passfile.readlines():
        user = line.split(':')[0]
        cryptPass = line.split(':')[1].strip('')
        print("Cracking Password For :", user)
        testPass(cryptPass)

if __name__ == '__main__':
    main()

