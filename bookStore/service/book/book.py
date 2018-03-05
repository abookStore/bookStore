# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import xlrd
from bookStore import db
from bookStore.mappings.book import Book
from bookStore.service.user.user import UserService


class BookService():

    def book_query_by_isbn(self, isbn):
        """
        根据 isbn 来搜索书目
        """
        if isbn:
            rows = db.session.query(Book).filter_by(
                isbn=isbn, is_active=1).all()
            book_info = {}
            books = {}
            for row in rows:
                book_info = {}
                book_info['id'] = row.id
                book_info['name'] = row.name
                book_info['author'] = row.author
                book_info['press'] = row.press
                book_info['isbn'] = row.isbn
                book_info['quantity'] = row.quantity
                book_info['description'] = row.description
                book_info['price'] = float(row.price)
                book_info['supplier_id'] = row.supplier_id
                book_info['supplier'] = row.supplier

                books[row.id] = book_info

            return books

        return None

    def book_query_by_name(self, name):
        """
        根据书名来搜索书目
        """
        if name:
            rows = db.session.query(Book).filter_by(name=name).all()

            book_info_all = {}
            for row in rows:
                book_info = {}
                book_info['id'] = row.id
                book_info['name'] = row.name
                book_info['author'] = row.author
                book_info['press'] = row.press
                book_info['isbn'] = row.isbn
                book_info['quantity'] = row.quantity
                book_info['description'] = row.description
                book_info['price'] = float(row.price)
                book_info['supplier_id'] = row.supplier_id
                book_info['supplier'] = row.supplier

                book_info_all[row.id] = book_info
            return book_info_all

        return None

    def book_query_by_id(self, book_id):
        """
        根据书目id来搜索书目
        """
        if book_id:
            row = db.session.query(Book).filter_by(id=book_id).first()

            book_info = {}
            book_info['id'] = row.id
            book_info['name'] = row.name
            book_info['author'] = row.author
            book_info['press'] = row.press
            book_info['isbn'] = row.isbn
            book_info['quantity'] = row.quantity
            book_info['description'] = row.description
            book_info['price'] = float(row.price)
            book_info['supplier_id'] = row.supplier_id
            book_info['supplier'] = row.supplier

            return book_info

        return None

    def book_query_by_isbn_and_supplier(self, isbn, supplier_id):
        """
        根据 supplier 和 isbn 来搜索唯一书目
        """
        if isbn and supplier_id:
            row = db.session.query(Book).filter_by(
                isbn=isbn, supplier_id=supplier_id, is_active=1).first()

            if row:
                book_info = {}
                book_info['id'] = row.id
                book_info['name'] = row.name
                book_info['author'] = row.author
                book_info['press'] = row.press
                book_info['isbn'] = row.isbn
                book_info['quantity'] = row.quantity
                book_info['description'] = row.description
                book_info['price'] = float(row.price)
                book_info['supplier_id'] = row.supplier_id
                book_info['supplier'] = row.supplier

                return book_info

        return None

    def book_add(self, user_id, book_info):
        """
        新增书目
        """
        if book_info:
            book = Book()
            book.isbn = book_info.get('isbn')
            book.name = book_info.get('name')
            book.author = book_info.get('author')
            book.press = book_info.get('press')
            book.quantity = book_info.get('quantity')
            book.description = book_info.get('description')
            book.price = book_info.get('price')
            book.supplier_id = user_id

            user_service = UserService()
            user_name = user_service.query_user_by_id(user_id).get('username')
            book.supplier = user_name
            book.is_active = 1

            db.session.add(book)
            db.session.flush(book)
            db.session.commit()

            return True

        return False

    def book_update(self, book_id, book_info):
        """
        更新书目信息
        """
        if book_id and book_info:
            book = db.session.query(Book).filter_by(id=book_id)
            if not book:
                return False

            book.isbn = book_info.get('isbn')
            book.name = book_info.get('name')
            book.author = book_info.get('author')
            book.press = book_info.get('press')
            book.quantity = book_info.get('quantity')
            book.price = book_info.get('price')
            book.description = book_info.get('description')

            db.session.flush(book)
            db.session.commit()

            return True

        return False

    def book_remove(self, book_id):
        """
        删除书目
        """
        if book_id:
            book = db.session.query(Book).filter_by(id=book_id)
            if not book:
                return False

            book.is_active = 0

            db.session.flush(book)
            db.session.commit()

            return True

        return False

    def book_quantity_update(self, book_id, quantity_inc):
        """
        书目库存的变化
        """
        if quantity_inc == 0:
            return True

        if not book_id:
            return False

        sql = """
        UPDATE book SET
        quantity = quantity + :quantity_inc
        WHERE id = :book_id
        AND quantity + :quantity_inc >= 0
        """
        params = {
            'quantity_inc': quantity_inc,
            'book_id': book_id
        }

        r = db.session.execute(sql, params).rowcount
        if r:
            return True

        return False

    def books_query_by_supplier(self, supplier_id):
        """
        单个供应商的书库里可提供的全部书目
        """
        rows = db.session.query(Book).filter_by(
            supplier_id=supplier_id, is_active=1).all()
        book_info = {}
        books = {}
        for row in rows:
            book_info = {}
            book_info['id'] = row.id
            book_info['name'] = row.name
            book_info['author'] = row.author
            book_info['press'] = row.press
            book_info['isbn'] = row.isbn
            book_info['quantity'] = row.quantity
            book_info['description'] = row.description
            book_info['price'] = float(row.price)
            book_info['supplier_id'] = row.supplier_id
            book_info['supplier'] = row.supplier

            books[row.id] = book_info
        return books

    def add_books_by_excel(self, user_id, file):
        """
        根据上传的 excel 更新书目库
        """
        user_service = UserService()
        user = user_service.query_user_by_id(user_id)
        try:
            df = pd.read_excel(file)
            for ix, row in df.iterrows():
                book = {}
                book['isbn'] = row.get('isbn')
                book['name'] = row.get('name')
                book['author'] = row.get('author')
                book['press'] = row.get('press')
                book['quantity'] = row.get('quantity')
                book['description'] = row.get('description')
                book['price'] = row.get('price')
                book['supplier_id'] = user_id
                book['supplier_name'] = user.get('username')

                # 判断是否存在
                old_book = self.book_query_by_isbn_and_supplier(
                    row.get('isbn'), user_id)

                if old_book:
                    self.book_update(old_book['id'], book)
                else:
                    self.book_add(user_id, book)

            return True

        except Exception:
            return False
