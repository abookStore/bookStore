# -*- coding: utf-8 -*-
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP, DECIMAL

from bookStore import db


class Admin(db.Model):
    """
    会员权限表
    """
    __table_name__ = 'admin'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    auth = Column(Integer)