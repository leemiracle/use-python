
class A:
    """
    staticmethod和classmethod：
        相同点:固定保存内存中
        不同点:
            staticmethod的保存地址和运行地址相同,classmethod的保存地址和运行地址不同；
            staticmethod装饰后的类型为function， classmethod装饰后的类型为method

    """

    a = 'lee'

    def __init__(self):
        self.b = 'miracle'

    @staticmethod
    def print_info(b='miracle'):
        a = A.a
        # print("from static_method  %s, %s" % (a, b))

    @classmethod
    def print_classmethod(cls, b='miracle'):
        A.print_info('he he')
        # print("from class_method %s, %s" % (cls.a, b))

A.print_info()
A.print_classmethod()
c = A()
c.print_info()
c.print_classmethod()

# 返回值
# from static_method  lee, miracle
# from static_method  lee, miracle
# from static_method  lee, he he
# from class_method lee, miracle
# from static_method  lee, he he
# from class_method lee, miracle

print(id(c.print_info()))
print(id(c.print_info))
print(id(c.print_classmethod()))
print(id(c.print_classmethod))
print('\n')

print(id(A.print_info()))
print(id(A.print_info))
print(id(A.print_classmethod()))
print(id(A.print_classmethod))
print('\n')

d = A()

print(id(d.print_info()))
print(id(d.print_info))
print(id(d.print_classmethod()))
print(id(d.print_classmethod))
print('\n')

# 打印：
# 9999216
# 140074107607784
# 9999216
# 140074107927240
#
#
# 9999216
# 140074107607784
# 9999216
# 140074107927240
#
#
# 9999216
# 140074107607784
# 9999216
# 140074107927240
print(type(d.print_info()))
print(type(d.print_info))
print(type(d.print_classmethod()))
print(type(d.print_classmethod))
# 返回
# <class 'NoneType'>
# <class 'function'>
# <class 'NoneType'>
# <class 'method'>
