"""
Skype数据库存储

SQLite3内部数据库格式

在 Windows 系统中,Skype 存储了的一个名叫 main.db 的数据库在路径 C:\Documents and Settings\<User>\ApplicationData\Skype\<Skype-account>目录下
"""

# 使用 sqlite3 命令行工具快速的连接到数据库:SELECT tbl_name FROM sqlite_master WHERE type==”table”;
#   SQL 函数datatime()可以将这种值转化为易懂的格式。

# Skype 数据库实际默认包含了所有用户发送和接受的信息。存储这些信息的为 Message 表。

