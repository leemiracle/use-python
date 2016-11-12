"""
蠕虫病毒: Conficker, W32DownandUp, Morris

莫里斯蠕虫包含了常用的用户名和密码
SSH 蠕虫

"""

# Conficker攻击向量:
#   Windows Server的0day 漏洞,蠕虫能够引起 堆栈溢出 从而能够执行 Shellcode 并下载一个副本给受到感染的主机。
#   Conficker 蠕虫尝试通过暴力破解默认的网络管理共享 (ADMIN$)来获取受害人主机的管理权限:
#       超过 250 个常用密码的密码列表
#       Morris 蠕虫曾使用的密码列表有 432 个密码
