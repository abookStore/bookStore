# -*- coding: utf-8 -*-
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP, DECIMAL

from bookStore import db


class ShoppingCart(db.Model):
    """
    购物车管理表
    """
    __table_name__ = 'shopping_cart'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    book_id = Column(Integer)
    book_name = Column(String)
    isbn = Column(Integer)
    supplier_id = Column(Integer)
    supplier = Column(String)
    origin_price = Column(DECIMAL)
    actual_price = Column(DECIMAL)
    total_price = Column(DECIMAL)
    discount = Column(DECIMAL)
    order_quantity = Column(Integer)
