from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint, Index

Base = declarative_base()


class UserPost(Base):
    """
    类的形式，建表
    """

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    insert_time = Column(DateTime)

    # 表名
    __tablename__ = 'users'
    # 表属性
    __table_args__ = (
        UniqueConstraint('user_id', 'post_id', name='uix_user_post_user_id_post_id'),
        Index('ix_user_post_user_id_insert_time', 'user_id', 'insert_time'),
    )
