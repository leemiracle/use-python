##处理流程
* 连接:engine = create_engine('sqlite:///:memory:', echo=True)
* 申明映射关系: Base = declarative_base()
* 创建数据库:Base.metadata.create_all(engine) User.__table__ (表信息)
* 为被映射的表创建个实例对象:ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
* 创建一个与数据库交互的会话：Session = sessionmaker(bind=engine)
* 添加和更新对象:session.add(ed_user),session.add_all(),session.dirty(列出session修改的对象),session.new(列出session新建的对象)，session.commit()
* 回滚:session.rollback()(回滚到sessio对象历史发生变化的前一节点)，fake_user in session(数据对象是否在session对象中)
* 查询:query(), label()(User.name.label('name_label')),aliased()(user_alias = aliased(User, name='user_alias')), filter_by(),filter()(== ,!=,like(),in_(),~表.字段.in_(),== None,and_(User.name == 'ed', User.fullname == 'Ed Jones')与条件，or_(User.name == 'ed', User.name == 'wendy')或条件，match('wendy')全文搜索、调用数据库的MATCH或CONTAINS函数、返回相似度)
* 返回列表和标量:all(),first(),one(),one_or_none(),scalar(),
* 使用SQL脚本: session.query(User).filter(text("id<:value and name=:name")).params(value=224,name='fred')
* 计数: session.query(User).filter(User.name.like('%ed')).count()或session.query(func.count('*')).select_from(User).scalar()
* 创建关系:user = relationship("User", back_populates="addresses"),user_id = Column(Integer, ForeignKey('users.id'))(user,user_id在Address类中), User.addresses = relationship("Address", order_by=Address.id, back_populates="user")
* 相关的对象之间的交互:jack = User(name='jack', fullname='Jack Bean', password='gjffdd'),jack.addresses = [Address(email_address='jack@google.com'),Address(email_address='j25@yahoo.com')]
* 通过Joins查询:session.query(User).join(Address).filter(Address.email_address=='jack@google.com')
* 使用别名:adalias1 = aliased(Address)
* 使用子查询：stmt = session.query(Address.user_id, func.count('*').label('address_count')).group_by(Address.user_id).subquery()，session.query(User, stmt.c.address_count).outerjoin(stmt, User.id==stmt.c.user_id).order_by(User.id)——————————》SELECT users.*,adr_count.address_count FROM users LEFT OUTER JOIN(SELECT user_id, count(*) AS address_count FROM addresses GROUP BY user_id) AS adr_count ON users.id=adr_count.user_id
* 从子查询中选择实体:
* 使用EXISTS:stmt = exists().where(Address.user_id==User.id),session.query(User.name).filter(stmt),使用".any()"来判断相关的实体是否存在（如session.query(User.name).filter(User.addresses.any())）,has()(类似any()多对一的关系),
* 公共关系型操作:__eq__() (many-to-one “equals” comparison)(query.filter(Address.user == someuser)),__ne__() (many-to-one “not equals” comparison),query.filter(Address.user == None),contains() (used for one-to-many collections),any() (used for collections),has() (used for scalar references),Query.with_parent() (used for any relationship)
* 预先加载:1.子查询加载 2.Joined加载 3.精确的Join + 预加载
* 删除:session.delete(jack)
* Configuring delete/delete-orphan Cascade:addresses = relationship("Address", back_populates='user',cascade="all, delete, delete-orphan"),(addresses在User类中)
* 建立多对多的关系:
