# 函数注释
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)


#-------修改原函数test_method------
# 原test_method改为test_method_1
def test_method_1(a):
    print(a)


def test_other_method(a):
    # 根据函数属性的不同，采取不同的处理逻辑
    if hasattr(test_other_method, 'publish'):
        print('i have')
    print("do thing")
    test_method_1(a)
    print('do other thing')


# test_method 为原函数
test_method = test_other_method
test_method_2 = test_other_method
# 修改函数属性
test_method_2.publish = 5
# ----------------

if __name__ == '__main__':
    test_method('here')
    test_method_2('iiiiii')


