# -*- coding: utf-8 -*-
from datetime import datetime
from bookStore import app, db
from bookStore.mappings.order import Order
from bookStore.mappings.order_detail import OrderDetail
from bookStore.mappings.order_info import OrderInfo
from bookStore.service.order.shopping_cart import CartService
from bookStore.service.user.address import AddressInfoService
from bookStore.service.user.account import AccountService
from bookStore.service.book.book import BookService
class OrderService():

    @staticmethod
    def order_query(uid):
        """
        根据用户名查询 全部order
        """
        payload = {}
        if uid:
            sql = """
            SELECT
                *
            FROM `order`
            WHERE user_id = :user_id
            ORDER BY id DESC
            """
            rows = db.session.execute(sql, {"user_id": uid}).fetchall()
            for row in rows:
                order = {
                    'order_id': row.order_id,
                    'user_id': row.user_id,
                    'quantity': row.quantity,
                    'origin_cost': float(row.origin_cost),
                    'actual_cost': float(row.actual_cost),
                    'order_status': row.order_status,
                    'delivery_status': row.delivery_status,
                    'pay_status': row.pay_status
                }
                payload[row.order_id] = order
            return payload

        raise NotImplementedError('不支持的查询方式')

    @staticmethod
    def order_query_by_uid_date(uid, order_id, status, from_date, to_date):
        """
        根据用户名查询 全部order
        """
        payload = {}
        if uid:
            sql = """
            SELECT
                *
            FROM `order`
            WHERE user_id = :user_id
            AND order_status = :status
            """
            if order_id:
                sql += 'AND order_id = :order_id\n'
            if from_date:
                sql += 'AND created_at >= :from_date\n'
            if to_date:
                sql += 'AND created_at <= :to_date\n'

            sql += 'ORDER BY id DESC'
            rows = db.session.execute(sql, {
                "user_id": uid,
                "status": status,
                "order_id": order_id,
                "from_date": from_date,
                "to_date": to_date
                }).fetchall()
            for row in rows:
                order = {
                    'order_id': row.order_id,
                    'user_id': row.user_id,
                    'quantity': row.quantity,
                    'origin_cost': float(row.origin_cost),
                    'actual_cost': float(row.actual_cost),
                    'order_status': row.order_status,
                    'delivery_status': row.delivery_status,
                    'pay_status': row.pay_status
                }
                payload[row.order_id] = order
            return payload

        raise NotImplementedError('不支持的查询方式')

    @staticmethod
    def order_ready_query_by_uid_date(uid, order_id, status, from_date, to_date):
        """
        根据用户名查询 待发货的order
        """
        payload = {}
        if uid:
            sql = """
            SELECT
                *
            FROM `order`
            WHERE user_id = :user_id
            AND order_status = :status
            AND delivery_status = 0
            AND pay_status = 1
            """
            if order_id:
                sql += 'AND order_id = :order_id\n'
            if from_date:
                sql += 'AND created_at >= :from_date\n'
            if to_date:
                sql += 'AND created_at <= :to_date\n'

            sql += 'ORDER BY id DESC'
            rows = db.session.execute(sql, {
                "user_id": uid,
                "status": status,
                "order_id": order_id,
                "from_date": from_date,
                "to_date": to_date
            }).fetchall()
            for row in rows:
                order = {
                    'order_id': row.order_id,
                    'user_id': row.user_id,
                    'quantity': row.quantity,
                    'origin_cost': float(row.origin_cost),
                    'actual_cost': float(row.actual_cost),
                    'order_status': row.order_status,
                    'delivery_status': row.delivery_status,
                    'pay_status': row.pay_status
                }
                payload[row.order_id] = order
            return payload

        raise NotImplementedError('不支持的查询方式')

    @staticmethod
    def order_detail_query(order_id):
        """
        根据订单名查询 订单的详细书目信息
        """
        payload = {}
        if order_id:
            sql = """
            SELECT
                *
            FROM order_detail
            WHERE order_id = :order_id
            ORDER BY id DESC
            """
            rows = db.session.execute(sql, {"order_id": order_id}).fetchall()
            for row in rows:
                order_detail = {
                    'order_id': row.order_id,
                    'book_name': row.book_name,
                    'isbn': row.isbn,
                    'origin_price': float(row.origin_price),
                    'actual_price': float(row.actual_price),
                    'discount': float(row.discount),
                    'order_quantity': row.order_quantity,
                    'deliveried_quantity': row.deliveried_quantity,
                    'warehouse': row.warehouse
                }
                payload[row.book_name] = order_detail
            return payload

        raise NotImplementedError('不支持的查询方式')

    @staticmethod
    def order_create(user_id, address_id):
        """
        新建订单
        """
        account_info = AccountService.account_query(user_id)
        cart = CartService()
        total_info = cart.cart_total(user_id)
        if account_info['balance'] < total_info['actual_cost']:
            return False, "余额不足"


        # 查询购物车
        books = cart.cart_info_query(user_id)
        if not books:
            return False, "购物车为空"

        # order 表
        order = Order()
        order_id = OrderService.generate_order_id()
        order.order_id = order_id
        order.user_id = user_id
        order.quantity = total_info['total_quantity']
        order.origin_cost = total_info['origin_cost']
        order.actual_cost = total_info['actual_cost']
        order.order_status = 1
        order.delivery_status = 0
        order.pay_status = 0

        db.session.add(order)
        db.session.flush()


        for book in books.values():
            # order_detail 表
            order_detail = OrderDetail()
            order_detail.order_id = order_id
            order_detail.book_id = book['book_id']
            order_detail.book_name = book['book_name']
            order_detail.isbn = book['isbn']
            order_detail.origin_price = book['origin_price']
            order_detail.actual_price = book['actual_price']
            order_detail.warehouse = book['supplier']
            order_detail.discount = book['discount']
            order_detail.order_quantity = book['order_quantity']
            order_detail.deliveried_quantity = 0

            db.session.add(order_detail)
            db.session.flush()

            # book 表修改库存书
            book_service = BookService()
            rowcount = book_service.book_quantity_update(book['book_id'], - book['order_quantity'])

            if rowcount is False:
                db.session.rollback()
                return False, "book_id : %s 库存不足，下单失败" % book['book_id']

        # order_info 表
        if not address_id:
            return False, "缺少收货地址id"

        address_service = AddressInfoService()
        address = address_service.address_query_by_id(user_id, address_id)
        order_info = OrderInfo()
        order_info.order_id = order_id
        order_info.consignee = address.name
        order_info.address = address.address
        order_info.post_code = address.post_code
        order_info.phone = address.phone
        db.session.add(order_info)
        db.session.flush()

        # account 表
        account_service = AccountService()
        change = - total_info['actual_cost']
        account_service.account_change(user_id, change)

        # account_consume 表
        balance = account_info['balance'] - total_info['actual_cost']
        account_service.account_consume_add(
            user_id,
            total_info['actual_cost'],
            balance
        )

        # 清空购物车
        cart.cart_remove_all(user_id)

        return True, '操作成功'

    @staticmethod
    def generate_order_id():
        """
        生成订单id
        """
        now = datetime.now().strftime("%Y%m%d%H%M%S")

        rand = ''
        import random
        for i in range(5):
            r = random.randint(0, 9)
            rand += str(r)

        return int(now + rand)
