# -*- coding: utf-8 -*-
import logging
import json
from flask import request
from flask_login import current_user, login_required
from bookStore import app
from bookStore.mappings.order import Order
from bookStore.mappings.order_detail import OrderDetail
from bookStore.service.order.order import OrderService
from bookStore.views.api import exports
from bookStore.views import make_api_response


@exports('/order/query', methods=['POST'])
@login_required
def query_orders():
    """
    @api {POST} /order/query 查询用户对应的订单信息
    @apiGroup Order
    @apiVersion 0.0.1
    @apiDescription 用于查询用户订单信息
    @apiParamExample {json} 请求样例：
                    {
                        ["orderId": "123"],
                        ["fromDate": "2018-02-01"],
                        ["toDate": "2018-03-01"]
                    }
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                        {
                            "payload": {
                                "12": {
                                "user_id": 123,
                                "order_id": 12,
                                "quantity": 1,
                                "origin_cost": 22.0,
                                "pay_status": 1,
                                "order_status": 1,
                                "actual_cost": 22.0,
                                "delivery_status": 1
                                }
                            },
                            "status": "ok"
                        }

    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    from_date = request.json.get('fromDate')
    to_date = request.json.get('toDate')
    order_id = request.json.get('order_id')

    user_id = current_user.id
    if not user_id:
        return make_api_response(message="用户不存在", statusCode=400)

    orders = OrderService.order_query_by_uid_date(user_id, order_id, 1, from_date, to_date)

    return make_api_response(payload=orders)


@exports('/order/closed_query', methods=['POST'])
@login_required
def query_closed_orders():
    """
    @api {POST} /order/closed_query 查询用户对应的已关闭的订单信息
    @apiGroup Order
    @apiVersion 0.0.1
    @apiDescription 查询用户对应的已关闭的订单信息
    @apiParamExample {json} 请求样例：
                    {
                        ["orderId": "123"],
                        ["fromDate": "2018-02-01"],
                        ["toDate": "2018-03-01"]
                    }
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                        {
                            "payload": {
                                "12": {
                                "user_id": 123,
                                "order_id": 12,
                                "quantity": 1,
                                "origin_cost": 22.0,
                                "pay_status": 1,
                                "order_status": 1,
                                "actual_cost": 22.0,
                                "delivery_status": 1
                                }
                            },
                            "status": "ok"
                        }

    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    from_date = request.json.get('fromDate')
    to_date = request.json.get('toDate')
    order_id = request.json.get('order_id')

    user_id = current_user.id
    if not user_id:
        return make_api_response(message="用户不存在", statusCode=400)

    orders = OrderService.order_query_by_uid_date(
        user_id, order_id, 0, from_date, to_date)

    return make_api_response(payload=orders)


@exports('/order/return_query', methods=['POST'])
@login_required
def query_return_orders():
    """
    @api {POST} /order/return_query 查询用户对应的退单信息
    @apiGroup Order
    @apiVersion 0.0.1
    @apiDescription 查询用户对应的退单信息
    @apiParamExample {json} 请求样例：
                    {
                        ["orderId": "123"],
                        ["fromDate": "2018-02-01"],
                        ["toDate": "2018-03-01"]
                    }
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                        {
                            "payload": {
                                "12": {
                                "user_id": 123,
                                "order_id": 12,
                                "quantity": 1,
                                "origin_cost": 22.0,
                                "pay_status": 1,
                                "order_status": 1,
                                "actual_cost": 22.0,
                                "delivery_status": 1
                                }
                            },
                            "status": "ok"
                        }

    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    from_date = request.json.get('fromDate')
    to_date = request.json.get('toDate')
    order_id = request.json.get('order_id')

    user_id = current_user.id
    if not user_id:
        return make_api_response(message="用户不存在", statusCode=400)

    orders = OrderService.order_query_by_uid_date(
        user_id, order_id, 2, from_date, to_date)

    return make_api_response(payload=orders)


@exports('/order/ready_query', methods=['POST'])
@login_required
def query_ready_orders():
    """
    @api {POST} /order/return_query 查询用户待发货的订单信息
    @apiGroup Order
    @apiVersion 0.0.1
    @apiDescription 查询用户待发货的订单信息
    @apiParamExample {json} 请求样例：
                    {
                        ["orderId": "123"],
                        ["fromDate": "2018-02-01"],
                        ["toDate": "2018-03-01"]
                    }
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                        {
                            "payload": {
                                "12": {
                                "user_id": 123,
                                "order_id": 12,
                                "quantity": 1,
                                "origin_cost": 22.0,
                                "pay_status": 1,
                                "order_status": 1,
                                "actual_cost": 22.0,
                                "delivery_status": 1
                                }
                            },
                            "status": "ok"
                        }

    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    from_date = request.json.get('fromDate')
    to_date = request.json.get('toDate')
    order_id = request.json.get('order_id')

    user_id = current_user.id
    if not user_id:
        return make_api_response(message="用户不存在", statusCode=400)

    orders = OrderService.order_ready_query_by_uid_date(
        user_id, order_id, 1, from_date, to_date)

    return make_api_response(payload=orders)

@exports('/order/detail/<order_id>', methods=['GET'])
@login_required
def query_order_detail(order_id):
    """
    @api {GET} /order/detail/<order_id> 查询订单对应的书目详情
    @apiGroup Order
    @apiVersion 0.0.1
    @apiDescription 用于查询用户订单信息
    @apiParam {String} order_id 订单id
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                        {
                            "payload": {
                                "论语": {
                                "isbn": 12311233,
                                "order_quantity": 42,
                                "book_name": "论语",
                                "origin_price": 1.0,
                                "discount": 3.0,
                                "warehouse": "北京2",
                                "actual_price": 22.0,
                                "order_id": 12,
                                "deliveried_quantity": 21
                                },
                                "诗经": {
                                "isbn": 12312321,
                                "order_quantity": 11,
                                "book_name": "诗经",
                                "origin_price": 12.0,
                                "discount": 2.0,
                                "warehouse": "北京1",
                                "actual_price": 123.0,
                                "order_id": 12,
                                "deliveried_quantity": 2
                                }
                            },
                            "status": "ok"
                        }

    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    # 获取参数
    if not order_id:
        return make_api_response(message='缺少order_id', statusCode=400)

    order_detail = OrderService.order_detail_query(order_id)

    if order_detail:
        return make_api_response(payload=order_detail)
    else:
        return make_api_response(message="订单不存在", statusCode=400)

@exports("/order/create", methods=["POST"])
# @login_required
def order_create():
    """
    创建订单
    """
    user_id = current_user.id
    if not user_id:
        return make_api_response(message="用户不存在", statusCode=400)

    origin_cost = request.json['origin_cost']
    actual_cost = request.json['actual_cost']
    total_quantity = request.json['total_quantity']
    address_id = request.json['address_id']

    total_info = {
        'origin_cost': origin_cost,
        'actual_cost': actual_cost,
        'total_quantity': total_quantity
    }

    result, message = OrderService.order_create(user_id, total_info, address_id)

    if not result:
        return make_api_response(message=message, statusCode=400)

    return make_api_response()