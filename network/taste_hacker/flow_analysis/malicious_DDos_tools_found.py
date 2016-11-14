"""
发现恶意的 DDos 工具

分析 LOIC 流量:
    LOIC 提供两种操作模式,第一中模式中,用户可以输入目标地址,第二种模式
称为 HIVEMIND,用户连接 LOIC 到一个目标的 IRC 服务将进行自动攻击
"""

import dpkt
import socket
import optparse

# 使用 Dpkt 找到谁在下载 LOIC

# 解析 HIVE 模式的 IRC 命令
#   IRC 服务使用的是 TCP 6667 端口,消息到 IRC 服务器的目的地至是 TCP 的 6667 端口
#   提取以太网协议,IP 协议和 TCP 协议。提取TCP 协议后,我们在探究特定的源和目的端口。如果看到命令!lazor 带有目的
# 端口 6667,我们就可以确认成员发送了攻击命令。如果我们看到!lazor 带有源目的地端口 6667,我们就可以确定服务器发送了成员攻击命令。,

# 识别正在进行的 DDos 攻击:
#   当一个用户开始了一个 LOIC 攻击,它将发送大量的 TCP 数据包给目标主机。这些数据包,接合从 HIVE 来的集体的数据包基本耗尽了目标
# 主机的资源。我们开始一个 tcpdump 会话看着每 0.00005 秒发送一个小的数据包。这种行为不断的重复直到攻击结束
#   为了发现一个攻击,我们将设置一个数据包阀值。如果一个用户到特定地址的的数据包数量超过该阀值,这表明我们将把它当做一个攻击做进一步调查。


def findDownload(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            tcp = ip.data
            http = dpkt.http.Request(tcp.data)
            if http.method == 'GET':
                uri = http.uri.lower()
            if '.zip' in uri and 'loic' in uri:
                print('[!] ' + src + ' Downloaded LOIC.')
        except:
            pass

THRESH = 10000
def findAttack(pcap):
    pktCount = {}
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport
            if dport == 80:
                stream = src + ':' + dst
            if pktCount.has_key(stream):
                pktCount[stream] = pktCount[stream] + 1
            else:
                pktCount[stream] = 1
        except:
            pass
        for stream in pktCount:
            pktsSent = pktCount[stream]
            if pktsSent > THRESH:
                src = stream.split(':')[0]
            dst = stream.split(':')[1]
            print('[+] ' + src + ' attacked ' + dst + ' with ' + str(pktsSent) + 'pkts.')


def findHivemind(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport
            sport = tcp.sport
            if dport == 6667:
                if '!lazor' in tcp.data.lower():
                    print('[!] DDoS Hivemind issued by: '+src)
                    print('[+] Target CMD: ' + tcp.data)
            if sport == 6667:
                if '!lazor' in tcp.data.lower():
                    print('[!] DDoS Hivemind issued to: '+src)
                    print('[+] Target CMD: ' + tcp.data)
        except:
            pass
