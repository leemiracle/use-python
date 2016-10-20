# 函数注释
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)


#-------修改原函数test_method------
# 原test_method改为test_method_1
def test_method_1(a):
    print(a)


def test_other_method(a):
    print("do thing")
    test_method_1(a)
    print('do other thing')

# test_method 为原函数
test_method = test_other_method
# ----------------


if __name__ == '__main__':
    test_method('here')


