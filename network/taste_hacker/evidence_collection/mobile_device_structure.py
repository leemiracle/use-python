"""
iTunes 备份

当用户对 iPhone 或者 iPad 设备进行备份时,它将文件存储到机器的特殊目录。
C:\Documents and Settings\<USERNAME>\Application Data\AppleComputer\MobileSync\Backup
"""

# 2011年IOS 系统事实上跟踪和记录设备的 GPS 坐标并存储在手机的 consolidated.db 数据库中。

# 为了获得关于每个文件更多的信息,我们将使用 UNIX 命令 file 来提取每个文件的文件类型。这个命令使用文件头的字节信息类确认文件类型。
#   定位文本消息数据库
#   file * ：确定当前文件夹下的文件类型
