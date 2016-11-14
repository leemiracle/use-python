"""
回收站
用 Python 来恢复回收站中删除的项目
"""

# 使用 OS 模块查找已删除的项目
import os


def returnDir():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None

# 将用户的 SID 关联起来
#   将使用 Windows 注册表将 SID 转化为一个准确的用户名。通过检查Windows
#   注册表键值 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\ProfileList\<SID>\ProfileImagePath,我们可以看到它返回
#   一个是%SystemDrive%\Documents and Settings\<USERID>。
