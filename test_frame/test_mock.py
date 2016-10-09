from unittest import mock, TestCase
# mock_object的返回值
values = {'a': 1}

# 方法一
class TestPartnerCompany(TestCase):
    # python_module.method为要mock掉的方法的调用路径
    @mock.patch.object(python_module, 'method')
    def test_method(self, mock_object):
        # mock_object替代掉method方法
        mock_object.return_value = values

# 方法二
mock_object = mock.Mock(return_value=values)
mock_patch = mock.patch.object(python_module,'method', new=mock_object)
mock_patch.start()
result = method(*args)
mock_patch.stop()

# 方法三
with mock.patch.object(python_module, 'query_wanxiang_data') as mock_object:
    mock_object.return_value = values
    result = method(*args)

