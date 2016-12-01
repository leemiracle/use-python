"""总代理模式"""

class ProcessProxy(object):
    def __init__(self):
        """
        解析器总代理
        """
        self.state_map = {}

    def add(self, processer):
        """
        添加解析器
        :param processer:
        :return:
        """
        self.state_map[(processer.type, processer.version)] = processer

    def parse(self, process_type, version, values):
        return self.state_map[(process_type, version)].parse(values)


class AbstractProcesser(object):
    """
    抽象的解析器类
    """

    version = None
    type = None

    def parse(self, company):
        """
        声明必须实现的方法
        """
        raise NotImplementedError


class GermanyProcesser(AbstractProcesser):
    version = 1
    type = 'DE'

    def parse(self, verified_company):
        pass

company_info_process = ProcessProxy()
company_info_process.add(GermanyProcesser())
