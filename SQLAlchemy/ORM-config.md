#映射配置

* 声明型映射:Base = declarative_base()
* 经典映射:mapper()
* Runtime Introspection of Mappings, Objects:inspect(User).all_orm_descriptors.keys()(结果为User的字段名)等价于Mapper.all_orm_descriptors


#关系配置
* 一对多
* 多对一
* 一对一
* 多对多
* 相关对象

# 扩展配置
*   Declarative Extension
*   Association Proxy
*		Hybrid Attributes
*		Automap
*		Mutable Scalars