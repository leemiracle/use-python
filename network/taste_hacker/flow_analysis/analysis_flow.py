"""
分析 Storm 的 Fast 流量和 Conficker 蠕虫的 Domain 流量

Fast 流量:利用 DNS 记录隐藏命令从而控制 Storm 僵尸网络。为了命令和控制主机,攻击者频繁的替换 IP 地址,确保 DNS 返回很短的 TTL 结果。

Conficker 蠕虫:攻击 Windows 的 SMB 协议漏洞来传播。一旦被感染,脆弱的主机连接到一个命名和控制服务器等待进一步指示。确认和阻止和命令控制主机通讯对于停止
攻击是完全有必要的。然而,Conficker 蠕虫使用当前的 UTC 时间和日期每三个小时就产生不同的域名。对 Conficker 迭代意味着每三个小时将产生50000 个域。攻击者只需要注册极少的域名到真是的 IP 就可以命令和控制服务
器。这使得拦截和阻止命令和控制服务器的流量很困难。因此技术人员将它命名为 Domain 流量。
http://www.cert.at/downloads/data/conficker_en.html
"""


# 使用 Scapy 解析 DNS 流量:包含在每一个 A 记录的DNSQR 包含了请求名(qname),请求类型(qtype)和请求类(qclass)。

# 练习 Fast 流量行为的例子的 PCAP:http://www.enisa.europa.eu/activities/cert/support/exercise/live-dvd-iso-images

# 用 Scapy 检测 Fast 流量: