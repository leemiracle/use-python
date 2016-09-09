
class BasicCustomization(object):
    """ 测试object类有多少属性 """
    pass


def test_basic_customization():
    """
    :return:
    """
    a = BasicCustomization()
    print("dir:", dir(a).__len__(), dir(a))


if __name__=='__main__':
    test_basic_customization()
