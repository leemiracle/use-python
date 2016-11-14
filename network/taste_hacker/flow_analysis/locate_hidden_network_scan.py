"""
找到隐藏的网络扫描

理解 TTL 字段:生存时间(TTL)字段用来确认一个 IP 数据包多跳可以到达目的地。数据包每通过一个路由器,路由器就减少一个 TTL 字段的值
LInux/Unix 系统上通常初始 TTL 值为 64,而 Windows 系统初始 TTL 值为128
"""

# Nmap 诱饵扫描

# 用 Scapy 解析 TTL 字段：有权限访问的主机TTL值正常，跟随特定路由设备路径。 无访问权限的主机的TTL值会出现异常(IP数据报的TTL值比系统初始值小1)

# coding=UTF-8
import time
import optparse
from scapy.all import *
from IPy import IP as IPTEST
ttlValues = {}
THRESH = 5

def checkTTL(ipsrc, ttl):
    if IPTEST(ipsrc).iptype() == 'PRIVATE':
        return
    if not ttlValues.has_key(ipsrc):
        pkt = sr1(IP(dst=ipsrc) / ICMP(), retry=0, timeout=1, verbose=0)
        ttlValues[ipsrc] = pkt.ttl

    if abs(int(ttl) - int(ttlValues[ipsrc])) > THRESH:
        print('\n[!] Detected Possible Spoofed Packet From: ' + ipsrc)
        print('[!] TTL: ' + ttl + ', Actual TTL: ' + str(ttlValues[ipsrc]))

def testTTL(pkt):
    try:
        if pkt.haslayer(IP):
            ipsrc = pkt.getlayer(IP).src
            ttl = str(pkt.ttl)
            print('[+] Pkt Received From: '+ipsrc+' with TTL: ' + ttl)
    except:
        pass

def main():
    parser = optparse.OptionParser("usage%prog -i<interface> -t <thresh>")
    parser.add_option('-i', dest='iface', type='string', help='specify network interface')
    parser.add_option('-t', dest='thresh', type='int', help='specify threshold count ')
    (options, args) = parser.parse_args()
    if options.iface == None:
        conf.iface = 'eth0'
    else:
        conf.iface = options.iface
    if options.thresh != None:
        THRESH = options.thresh
    else:
        THRESH = 5
    sniff(prn=testTTL, store=0)

if __name__ == '__main__':
    main()

