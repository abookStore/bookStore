# -*- coding:utf-8 -*-

from bookStore import db, app
from bookStore.mappings.shopping_cart import ShoppingCart
from bookStore.service.book.book import BookService
from bookStore.service.user.account import AccountService


class CartService():
    def cart_info_query(self, user_id):
        """
        查询购物车内的书目信息
        """
        cart = {}
        if user_id:
            rows = db.session.query(ShoppingCart).filter_by(
                user_id=user_id).all()

            if rows:
                for row in rows:
                    book = {}
                    book['id'] = row.id
                    book['user_id'] = row.user_id
                    book['book_id'] = row.book_id
                    book['book_name'] = row.book_name
                    book['isbn'] = row.isbn
                    book['supplier'] = row.supplier
                    book['origin_price'] = float(row.origin_price)
                    book['actual_price'] = float(row.actual_price)
                    book['total_price'] = float(row.total_price)
                    book['discount'] = float(row.discount)
                    book['order_quantity'] = row.order_quantity

                    cart[row.id] = book

            return cart

        return None

    def cart_add(self, user_id, book_id, quantity):
        """
        购物车新增书目
        """
        if not user_id or not book_id or not quantity:
            return False

        book_service = BookService()
        book = book_service.book_query_by_id(book_id)
        price = book['price']
        account_service = AccountService()
        account = account_service.account_query(user_id)
        discount = account['discount']

        cart = ShoppingCart()
        cart.user_id = user_id
        cart.book_id = book_id
        cart.book_name = book['name']
        cart.isbn = book['isbn']
        cart.supplier = book['supplier']
        cart.origin_price = price
        cart.order_quantity = quantity
        cart.discount = discount
        cart.actual_price = price * discount
        cart.total_price = price * quantity * discount

        db.session.add(cart)
        db.session.flush()
        db.session.commit()

        return False

    def cart_quantity_update(self, quantity, cart_id, user_id):
        """
        变更购物车内书目的数量
        """
        if cart_id:
            sql = """
            UPDATE shopping_cart
            SET
                order_quantity = :quantity,
                total_price = actual_price * :quantity
            WHERE id = :cart_id
            AND user_id = :user_id
            LIMIT 1
            """

            params = {
                "quantity": quantity,
                "cart_id": cart_id,
                "user_id": user_id
            }

            db.session.execute(sql, params)
            db.session.commit()

            return True
        return False

    def cart_remove(self, user_id, cart_id):
        """
        删除购物车中指定书目
        """
        sql = """
        DELETE FROM shopping_cart
        WHERE id = :cart_id
        LIMIT 1;
        """
        if cart_id:
            db.session.execute(sql, {'cart_id': cart_id})
            db.session.commit()

            return True

        return False

    def cart_remove_all(self, user_id):
        """
        清空购物车
        """
        sql = """
        DELETE FROM shopping_cart
        WHERE user_id = :user_id
        """
        if user_id:
            db.session.execute(sql, {'user_id': user_id})
            db.session.commit()

            return True

        return False

    def cart_quantity(self, user_id):
        """
        计算购物车中综合
        """
        sql = """
        SELECT
            SUM(order_quantity)
        FROM shopping_cart
        WHERE user_id = :user_id
        """
        if user_id:
            total_quantity = db.session.execute(sql, {'user_id': user_id}).scalar()

            return total_quantity

        return None
