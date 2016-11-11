import socket
import sys
import os

if len(sys.argv)==2:
    """sys 提供 访问和维护 python 解释器的能力"""
    filename = sys.argv[1]

    if not os.path.isfile(filename):
        """os 提供了丰富的与 MAC,NT,Posix 等操作系统进行交互的能力"""
        print('[-] ' + filename + ' does not exist.')
        exit(0)
    if not os.access(filename, os.R_OK):
        print('[-] ' + filename + ' access denied.')
        exit(0)
    print("[+] Reading Vulnerabilities From: " + filename)

def retBanner(ip, port):
    """socket:检测目标ip是否开启 某端口服务"""
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        banner = str(banner)
        return banner
    except:
        return


def main():
    """扫描"""
    ip1 = '192.168.95.148'
    ip2 = '192.168.95.149'
    port = 21
    banner1 = retBanner(ip1, port)
    if banner1:
        print('[+] ' + ip1 + ': ' + str(banner1))
        checkVulns(banner1)
    banner2 = retBanner(ip2, port)
    if banner2:
        print('[+] ' + ip2 + ': ' + str(banner2))
        checkVulns(banner2)


def checkVulns(banner):
    """I/O:检测是否存在已知漏洞：写入vuln_banners.txt文件中"""
    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
        print('[+] FreeFloat FTP Server is vulnerable.')
    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print('[+] 3CDaemon FTP Server is vulnerable.')
    elif 'Ability Server 2.34' in banner:
        print('[+] Ability FTP Server is vulnerable.')
    elif 'Sami FTP Server 2.0.2' in banner:
        print('[+] Sami FTP Server is vulnerable.')
    else:
        print('[-] FTP Server is not vulnerable.')
    return

if __name__ == '__main__':
    main()
