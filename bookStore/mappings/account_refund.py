# -*- coding: utf-8 -*-
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP, DECIMAL

from bookStore import db


class AccountRefund(db.Model):
    """
    登录会员表
    """
    __table_name__ = 'account_refund'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    amount = Column(DECIMAL)
    current_balance = Column(DECIMAL)
    day = Column(Integer)
    month = Column(Integer)
