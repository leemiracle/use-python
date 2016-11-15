"""
躲避杀毒软件

大多数杀毒软件只要是将基于签名检测作为主要的检测方法

"""

# 使用简单的 Windows 绑定 shell,将绑定 cmd.exe 到 TCP 端口:这允许攻击者远程连接到主机并发出命令和 cmd.exe 程序相交互。

# 接下来,我们写一个脚本执行这个 C 风格 shellcode。Python 允许导入外来函数的库。我们可以导入 ctypes 库,它允许我们和 C 语言的数据类型交互。

# 让我们通过Pyinstaller 编译软件提高它。(可以从:http://www.pyinstaller.org/获得)。Pyinstaller 将 Python 脚本编译为独立的可执行程序,可以分发给没有安装Python 解释器的系统使用。

# 接下来,我们将指导 Pyinstaller 建立一个说明文件为 Windows 的可执行文件做准备,我们将指示 Pyinstaller 不显示一个控制台用 --noconsole 选项,最终构建一个最终的可执行程序到一个单独的文件用
# --onefile 选项。

# 接下来,建立了说明文件后,我们将指示 Pyinstaller 建立一个可执行文件分发给我们的受害者。Pyinstaller 创建一个名为 bindshell.exe 的可执行程序在目录bindshell\dist\下,
# 我们现在可以分发这个可执行程序给任何 Windows 32 位系统的受害者。

# 验证躲避
