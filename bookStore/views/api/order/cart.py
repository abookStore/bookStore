# -*- coding: utf-8 -*-
import logging

from flask import request
from flask_login import current_user, login_required

from bookStore import app
from bookStore.service.order.shopping_cart import CartService
from bookStore.views.api import exports
from bookStore.views import make_api_response


@exports('/cart/query', methods=['GET'])
@login_required
def query_cart():
    """
    @api {GET} /cart/query 查询用户购物车信息
    @apiGroup Cart
    @apiVersion 0.0.1
    @apiDescription 查询用户购物车信息
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                    {
                        "payload": {
                            "4": {
                                "discount": 1.0, 
                                "user_id": 4, 
                                "book_id": 1, 
                                "id": 4, 
                                "origin_price": 0.0, 
                                "supplier": "供货商1", 
                                "total_price": 20.33, 
                                "isbn": 9203204223, 
                                "book_name": "论语", 
                                "actual_price": 12.23, 
                                "order_quantity": 15,
                                "quantity": 20
                            }, 
                            "5": {
                                "discount": 1.0, 
                                "user_id": 4, 
                                "book_id": 1, 
                                "id": 5, 
                                "origin_price": 0.0, 
                                "supplier": "234", 
                                "total_price": 43.0, 
                                "isbn": 23123213, 
                                "book_name": "haha", 
                                "actual_price": 32.0, 
                                "order_quantity": 23,
                                "quantity": 25
                                }
                        }, 
                        "status": "ok"
                    }
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    user_id = current_user.id
    if user_id:
        cart_service = CartService()
        cart = cart_service.cart_info_query(user_id)

        return make_api_response(payload=cart)

    return make_api_response(message="用户不存在", statusCode=400)


@exports('/cart/add', methods=['POST'])
@login_required
def add_cart():
    """
    @api {POST} /cart/add 添加书目到购物车
    @apiGroup Cart
    @apiVersion 0.0.1
    @apiDescription 添加书目到购物车
    @apiParam {int} book_id 书目的id
    @apiParam {int} quantity 数量
    @apiParamExample {json} 请求样例：
                        {
                            "book_id": 1,
                            "quantity": 12
                        }
    @apiSuccess (200) {String} msg 信息
    """
    user_id = current_user.id
    book_id = request.json['book_id']
    quantity = request.json['quantity']

    cart_service = CartService()

    cart_service.cart_add(user_id, book_id, quantity)

    return make_api_response()


@exports('/cart/update', methods=['POST'])
@login_required
def update_address_info():
    """
    @api {POST} /cart/update 更新购物车
    @apiGroup Cart
    @apiVersion 0.0.1
    @apiDescription 更新购物车
    @apiParam {int} cart_id 购物车item的编号
    @apiParam {int} quantity 数量
    @apiParamExample {json} 请求样例：
                        {
                            "cart_id": 1,
                            "quantity": 12
                        }
    @apiSuccess (200) {String} msg 信息
    """

    user_id = current_user.id
    cart_id = request.json['cart_id']
    quantity = request.json['quantity']

    cart_service = CartService()

    cart_service.cart_quantity_update(quantity, cart_id, user_id)

    return make_api_response()


@exports('/cart/remove/<cart_id>', methods=['GET'])
@login_required
def remove_cart_item(cart_id):
    """
    @api {GET} /cart/remove/<address_id> 删除购物车中某条信息
    @apiGroup Cart
    @apiVersion 0.0.1
    @apiDescription 删除购物车中某条信息
    @apiParam {int} cart_id 购物车中item编号
    @apiSuccess (200) {String} msg 信息
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    user_id = current_user.id
    cart_service = CartService()

    rv = cart_service.cart_remove(user_id, cart_id)

    if not rv:
        return make_api_response(statusCode=400)

    return make_api_response()


@exports('/cart/remove_all', methods=['GET'])
@login_required
def remove_cart():
    """
    @api {GET} /cart/remove_all 清空购物车
    @apiGroup Cart
    @apiVersion 0.0.1
    @apiDescription 清空购物车
    @apiSuccess (200) {String} msg 信息
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    user_id = current_user.id
    cart_service = CartService()

    if not user_id:
        return make_api_response(message="用户不存在", statusCode=400)
    rv = cart_service.cart_remove_all(user_id)

    if not rv:
        return make_api_response(statusCode=400)

    return make_api_response()
