""" 将json中的驼峰命名的字符串转换成pythonic code"""


import re

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


def camelcase_to_underscore(name):
    """
    将驼峰命名转换为pythonic
    :param name:
    :return:
    """
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()


def deep_camelcase_to_underscore(obj):
    if isinstance(obj, dict):
        new_obj = {camelcase_to_underscore(key): deep_camelcase_to_underscore(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        new_obj = [deep_camelcase_to_underscore(item) for item in obj]
    else:
        new_obj = obj
    return new_obj

if __name__ == "__main__":
    obj = {
        "error_code": 0,
        "reason": "ok",
        "result": {
            "baseInfo": {
                "base": "浙江",
                "businessScope": "许可经营项目：娃哈哈系列产品的生产、销售。  一般经营项目：按经贸部批准的目录，以原杭州娃哈哈集团公司名义经营集团公司及成员企业自产产品、相关技术出口业务和生产所需原辅材料、机械设备、仪器仪表、零配件等商品及相关技术的进口业务，开展“三来一补”业务。商业、饮食业、服务业的投资开发；建筑材料、金属材料、机电设备、家用电器、化工产品（不含危险品及易制毒品）、计算机软硬件及外部设备、电子元器件、仪器仪表的销售；生物工程技术、机电产品、计算机技术开发及咨询服务，物资仓储（不含危险品）,旅游接待服务。",
                "companyOrgType": "其他有限责任公司",
                "estiblishTime": 728668800000,
                "fromTime": 728668800000,
                "id": 47183021,
                "legalPersonName": "宗庆后",
                "name": "杭州娃哈哈集团有限公司",
                "regCapital": "52637.47 万元人民币",
                "regInstitute": "浙江省工商行政管理局",
                "regLocation": "杭州市清泰街160号",
                "regNumber": "330000000032256",
                "regStatus": "存续"
            },
            "investorList": [
                {
                    "amount": 0,
                    "name": "宗庆后",
                    "type": "个人"
                },
                {
                    "amount": 0,
                    "id": 47183477,
                    "name": "杭州上城区投资控股集团有限公司",
                    "type": "公司"
                },
            ],
            "investList": [
                {
                    "amount": 480.2,
                    "id": 385687839,
                    "name": "白山娃哈哈饮料有限公司"
                },
                {
                    "amount": 0,
                    "id": 1452244152,
                    "name": "杭州娃哈哈非常可乐饮料有限公司"
                },
            ],
            "staffList": [
                {
                    "name": "王国民",
                    "staffName": [
                        "董事"
                    ]
                },
                {
                    "name": "宗庆后",
                    "staffName": [
                        "董事长"
                    ]
                }
            ],
            "branchList": [
                {
                    "id": 47185546,
                    "name": "杭州娃哈哈集团有限公司销售分公司"
                }
            ]
        }
    }
    new_obj = deep_camelcase_to_underscore(obj)
    print(new_obj)