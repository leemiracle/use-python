"""
需要在系统中安装clamav,clamav-daemon,并注册服务
"""
import pyclamd
cd = pyclamd.ClamdAgnostic()
cd.ping()
print(cd.version().split()[0])
print(cd.reload())
print(cd.stats().split()[0])
# 写病毒特征码
void = open('/tmp/EICAR', 'wb').write(cd.EICAR())
void = open('/tmp/NO_EICAR', 'w').write('no virus in this file')
result = cd.scan_file('/tmp/EICAR')
print("scan_file:", cd.scan_file('/tmp/NO_EICAR') is None)
# 扫描病毒特征码 流文件
print("scan_stream:", cd.scan_stream(cd.EICAR()))