"""
Nmap:扫描
Nlog：

google 地图更加精确：使用 Python 建立 Google 地图

MaxMind:免费的数据库，在 http://www.maxmind.com/app/geolitecity 可获得,为我们提供了足够的精确度从 IP 地址到物理地址
"""

import dpkt
import socket
import pygeoip

# 使用 PyGeoIP 关联 IP 地址到物理地址
#    Jennifer Ennis 制作了一个纯 Python 模块用来查询 GeoLiteCity 数据库
#    用本地的 GeoIP 的位置。接下来我们将为特殊的记录指定 IP 地址查询数据库。它将返回一个记录包含城市(city),地区名(region_name),邮编(postal_code),
# 国家(country_name),经纬度(latitude and longitude)以及其他的确认信息。


gi = pygeoip.GeoIP('/opt/GeoIP/GeoIP.dat')


def retGeoStr(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country_code3']
        if city != '':
            geoLoc = city + ', ' + country
        else:
            geoLoc = country
        return geoLoc
    except Exception as e:
        return 'Unregistered'

# 使用 Dpkt 解析数据包 在 Windows 或者 Mac OS X 系统上：使用 Scapy 数据包操作工具来分析和制作数据包
#   Dpkt 允许我们遍历每一个捕获的数据包并检查每一个协议层。

# pypcap 分析流量：


def printPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print('[+] Src: ' + src + ' --> Dst: ' + dst)
        except:
            pass

def main():
    f = open('data.pcap')
    pcap = dpkt.pcap.Reader(f)
    printPcap(pcap)

if __name__ == '__main__':
    main()
