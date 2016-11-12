"""
端口扫描器：编程语言提供了访问 BCD 套接字的接口(python socket)->socket API->TCP/IP 套接字

结合 Nmap 扫瞄器:标准的扫描工具包(ACK, RST, FIN, or SYN-ACK)

TCP SYN 扫描 :又称为半开放扫描,这种类型的扫描发送一个 SYN 的TCP 连接数包等待响应,当返回 RST 数据包表示端口关闭,返回 ACK 数据包表示端口开放。
TCP NULL 扫描 :TCP 空扫描设置 TCP 的标志头为零。如果返回一个 RST 数据包则表示这个端口是关闭的。
TCP FIN 扫描 : TCP FIN 扫描发送一个 FIN 数据包,主动关闭连接,等待一个圆满的终止,如果返回 RST 数据包则表示端口是关闭的。
TCP XMAS 扫描 :TCP XMAS 扫描设置 PSH, FIN,和 URG TCP 标志位,如返回 RST 数据包则表示这个端口是关闭的。

Web 服务可能运行在 TCP 的 80 端口
邮件服务可能运行在 TCP 的 25 端口
文件传输服务可能运行在 TCP 的 21 端口
"""

# 第一步,我们要输入目标主机名和要扫描的常用端口列表。

# 通过目标主机名得到目标的网络 IP 地址

# 用列表里面的每一个端口去连接目标地址

# 确定端口上运行的特殊服务

# 发送特定的数据,并读取特定应用程序返回的标识| 了解具体是什么程序哪个版本占用了端口

# 多线程扫描 | 提高扫描效率

# coding=UTF-8
import optparse
import socket
import threading
screenLock = threading.Semaphore(value=1)


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print('[+]%d/tcp open' % tgtPort)
        print('[+] ' + str(results))
    except:
        screenLock.acquire()
        print('[-]%d/tcp closed' % tgtPort)
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unknown host"%tgtHost)
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[+] Scan Results for: ' + tgtIP)
    socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port ' + str(tgtPort))
    t = threading.Thread(target=connScan,
                         args=(tgtHost, int(tgtPort)))

    t.start()


def main():
    parser = optparse.OptionParser('usage %prog –H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='int', help='specify target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    args.append(tgtPort)
    if (tgtHost == None) | (tgtPort == None):
        print('[-] You must specify a target host and port[s]!')
    exit(0)
    portScan(tgtHost, args)

if __name__ == '__main__':
    main()
