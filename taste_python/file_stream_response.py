"""
作用：解决response文件流，所带的文件名不能带中文等特殊字符
例如：flask
"""
from flask import make_response
from urllib.parse import quote

template_name = '中文.pdf'
# 中文转url编码
template_name = quote(template_name)
response = make_response()
response.headers['Content-Type'] = 'application/pdf;charset=utf-8'
response.headers['Content-Disposition'] = "attachment; filename*=UTF-8''%s.pdf" % template_name
