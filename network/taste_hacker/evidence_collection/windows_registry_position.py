"""
windows注册表：包含了一个存储操作系统配置设置的层次化数据库
"""

# 注册表存储每一个网络信息在HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\NetworkList\Signatures\Unmanaged 子键值下。从
# Windows 命令提示符,我们可以列出每一个网络显示描述 GUID,网络描述,网络名称和网关 MAC 地址。

# 使用 WinReg 读取 Windows 注册表

# 使用 Mechanize 将 MAC 地址提交到 Wigle

# 以前连接过的无线接入点并查询他们的物理位置

# coding=UTF-8
import optparse
import mechanize
import urllib
import re
import _winreg

def val2addr(val):
    addr = ""
    for ch in val:
        addr += ("%02x " % ord(ch))
        addr = addr.strip(" ").replace(" ", ":")[0:17]
    return addr


def wiglePrint(username, password, netid):
    browser = mechanize.Browser()
    browser.open('http://wigle.net')
    reqData = urllib.urlencode({'credential_0': username, 'credential_1': password})
    browser.open('https://wigle.net/gps/gps/main/login', reqData)
    params = {}
    params['netid'] = netid
    reqParams = urllib.urlencode(params)
    respURL = 'http://wigle.net/gps/gps/main/confirmquery/'
    resp = browser.open(respURL, reqParams).read()
    mapLat = 'N/A'
    mapLon = 'N/A'
    rLat = re.findall(r'maplat=.*\&', resp)
    if rLat:
        mapLat = rLat[0].split('&')[0].split('=')[1]
    rLon = re.findall(r'maplon=.*\&', resp)
    if rLon:
        mapLon = rLon[0].split
    print('[-] Lat: ' + mapLat + ', Lon: ' + mapLon)


def printNets(username, password):
    net = "SOFTWARE\Microsoft\WindowsNT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
    net)
    print('\n[*] Networks You have Joined.')
    for i in range(100):
        try:
            guid = _winreg.EnumKey(key, i)
            netKey = _winreg.OpenKey(key, str(guid))
            (n, addr, t) = _winreg.EnumValue(netKey, 5)
            (n, name, t) = _winreg.EnumValue(netKey, 4)
            macAddr = val2addr(addr)
            netName = str(name)
            print('[+] ' + netName + ' ' + macAddr)
            wiglePrint(username, password, macAddr)
            _winreg.CloseKey(netKey)
        except:
            break

def main():
    parser = optparse.OptionParser("usage%prog -u <wigle username> -p <wigle password>")
    parser.add_option('-u', dest='username', type='string', help='specify wigle password')
    parser.add_option('-p', dest='password', type='string', help='specify wigle username')
    (options, args) = parser.parse_args()
    username = options.username
    password = options.password
    if username == None or password == None:
        print(parser.usage)
        exit(0)
    else:
        printNets(username, password)

if __name__ == '__main__':
    main()
