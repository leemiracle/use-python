# RESTful 用于快速创建 REST APIs
#### 主页：https://github.com/flask-restful/flask-restful/
## 解析请求
####reqparse:仿照的argparse 接口.
#####它属性和方法：
#####RequestParser().add_argument()[静态设置请求需要添加的参数]：location='headers'指定在请求头中取数据，
#####RequestParser().parse_args()[获取请求的值（字典）]
#####RequestParser().copy()[继承RequestParser]
#####parser = reqparse.RequestParser(bundle_errors=True)或者配置app.config['BUNDLE_ERRORS'] = True[错误绑定到一起，并一次全部返回给客户端,False时马上退出]

## 参数字段
####Fields:字段名, 字段类型
## Flask-RESTful的扩展
####内容交互:api = Api(app)
####自定义字段、输入、输出:
####方法装饰
####错误处理
## 使用中间件
####flask的最佳实践