# coding=UTF-8

"""
Pexpect: tool for controlling other applications.

可以用来实现与 ssh、ftp、telnet 等程序的自动交互;可以用来自动复制软件安装包并在不同机器自动安装;还可以用来实现软件测试中与命令行交互的自动化
"""
# ssh root@127.0.0.1
# Are you sure you want to continue connecting (yes/no)? yes
# Password:**************
# uname -v

import pexpect
PROMPT = ['# ', '>>> ', '> ', '\$ ']


def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:
        print('[-] Error Connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
    if ret == 0:
        print('[-] Error Connecting')
        return
    child.sendline(password)
    child.expect(PROMPT)
    return child

def main():
    host = 'localhost'
    user = 'root'
    password = 'toor'
    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root')


if __name__ == '__main__':
    main()
