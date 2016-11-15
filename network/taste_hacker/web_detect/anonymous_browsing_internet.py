"""
匿名浏览互联网

python:Mechanize(John J. Lee)

Linux:wget

"""

# 匿名---增加代理,用户代理和 Cookies
#   网站查找唯一标识符来识别网页游客有几种不同的方法:
#       1.第一种方法是通过记录请求的 IP 来确认用户。这可以通过使用虚拟专用网络(VPN)或者 tor 网络来缓和。一旦一个客户连接到 VPN,然后,所有的将通过 VPN 自动处理。
#       2.站点使用浏览器的 user-agent 字符串来识别唯一用户另一种方法。在正常情况下,user-agent 字符串让网站知道关于浏览器的重要信息能制作 HTML 代码给用户更好的体验。
# 然而,这些信息柏包含内核版本,浏览器版本,和其他关于用户的详细信息。恶意网站利用这些信息针对特定的浏览器进行精密的渗透利用,而其他网站利用这些信息来区分电脑是位与 NAT 网络还是私有网络。
#       3.网站会返回一些包含独特标识的 cookie 给 WEB 浏览器允许网站识别重复的重复的访客。为了防止这一点,我们将执行其他函数从我们的 WEB 浏览器中清除 cookie

# HTTP 代理:(http://www.hidemyass.com/),http://rmccurdy.com/scripts/proxy/good.txt

# 用匿名类抹去 WEB 页面

# 用 Beautiful Soup 解析 Href 链接:(1)利用正则表达式来搜索和替换HTML 代码。(2)使用强大的第三方库 BeautifulSoup

# 用 Beautiful Soup 下载图片

