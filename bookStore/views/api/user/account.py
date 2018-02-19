# -*- coding: utf-8 -*-
import logging

from flask import request
from flask_login import current_user, login_required

from bookStore import app
from bookStore.service.user.account import AccountService
from bookStore.views.api import exports
from bookStore.views import make_api_response


@exports('/account/query', methods=['GET'])
@login_required
def query_user_info():
    """
    @api {GET} /account/query 查询用户账户信息
    @apiGroup Users
    @apiVersion 0.0.1
    @apiDescription 用于查询用户资料
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                   {
                        "status": "ok",
                        "payload":{
                            "user_id": "132",
                            "balance": "1283.23",
                            "bonus_point": "3000",
                            "discount": "0.75"
                        }
                    }
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    user_id = current_user.id
    app.logger.info(user_id)
    account_info = AccountService.account_query(user_id=user_id)

    if account_info:
        return make_api_response(payload=account_info)
    else:
        return make_api_response(message="用户不存在", statusCode=400)


@exports('/accountlog/query', methods=['GET'])
@login_required
def query_user_account_log():
    """
    @api {GET} /accountlog/query 查询用户账户信息
    @apiGroup Users
    @apiVersion 0.0.1
    @apiDescription 用于查询用户消费记录
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                    {
                        "status": "ok", 
                        "payload": {
                            "2018-02-17 04:54:30": {
                            "created_at": "2018-02-17 04:54:30", 
                            "user_id": 4, 
                            "current_balance": 14380.0, 
                            "amount": 4380.0, 
                            "type": "充值"
                            }, 
                            "2018-02-17 04:58:41": {
                            "created_at": "2018-02-17 04:58:41", 
                            "user_id": 4, 
                            "current_balance": 14180.0, 
                            "amount": 150.0, 
                            "type": "退款"
                            }
                        }
                    }
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    user_id = current_user.id
    if not user_id:
        return make_api_response(message="用户不存在", statusCode=400)

    account_service = AccountService()
    account_logs = account_service.account_log_query(user_id=user_id)

    return make_api_response(payload=account_logs)


@exports('/account_consume/query', methods=['GET'])
@login_required
def query_account_consume():
    user_id = current_user.id

    account_service = AccountService()
    rvs = account_service.account_consume_query(user_id)

    if not rvs:
        return make_api_response()

    payload = {}
    for rv in rvs:
        consume = {}
        consume[rv.id] = rv.id
        consume[rv.amount] = rv.amount
        consume[rv.current_balance] = rv.current_balance

        payload[rv.id] = consume

    return payload


@exports('/account_prepare/query', methods=['GET'])
@login_required
def query_account_prepare():
    user_id = current_user.id

    account_service = AccountService()
    rvs = account_service.account_prepay_query(user_id)

    if not rvs:
        return make_api_response()

    payload = {}
    for rv in rvs:
        consume = {}
        consume[rv.id] = rv.id
        consume[rv.amount] = rv.amount
        consume[rv.current_balance] = rv.current_balance

        payload[rv.id] = consume

    return payload

@exports('/account_refund/query', methods=['GET'])
@login_required
def query_account_refund():
    user_id = current_user.id

    account_service = AccountService()
    rvs = account_service.account_refund_query(user_id)

    if not rvs:
        return make_api_response()

    payload = {}
    for rv in rvs:
        consume = {}
        consume[rv.id] = rv.id
        consume[rv.amount] = rv.amount
        consume[rv.current_balance] = rv.current_balance

        payload[rv.id] = consume

    return payload
