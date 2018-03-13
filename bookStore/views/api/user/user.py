# -*- coding: utf-8 -*-
import logging

from flask import request
from flask_login import current_user, login_required
from bookStore.service.user.user import UserService
from bookStore.views.api import exports
from bookStore.views import make_api_response


@exports('/user/query/<username>', methods=['GET'])
@login_required
def query_user_info(username):
    """
    @api {GET} /user/query/<username> 根据用户名查询用户信息
    @apiGroup Users
    @apiVersion 0.0.1
    @apiDescription 根据用户名查询用户信息
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiParam {String} username 用户账户名
    @apiSuccessExample {json} 返回样例:
                   {
                        "status": "ok",
                        "payload":{
                            "realname": "132",
                            "username": "bs",
                            "phone": "pwd",
                            "mail": "xxx@xxx.com",
                            "nickname": "guest",
                            "gender": "23",
                            "password": "pwd",
                            "qq": "12312"
                        }
                    }
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    user_id = current_user.id
    userinfo = UserService.query_user_by_name(username=username)

    if userinfo:
        return make_api_response(payload=userinfo)
    else:
        return make_api_response(message="用户不存在", statusCode=400)


@exports('/user/query/all', methods=['GET'])
@login_required
def query_user_all(username):
    """
    @api {GET} /user/query/all 查询系统中所有的卖家
    @apiGroup Users
    @apiVersion 0.0.1
    @apiDescription 查询系统中所有的卖家
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiParam {String} username 用户账户名
    @apiSuccessExample {json} 返回样例:
                   {
                        "status": "ok",
                        "payload":{
                            "realname": "132",
                            "username": "bs",
                            "phone": "pwd",
                            "mail": "xxx@xxx.com",
                            "nickname": "guest",
                            "gender": "23",
                            "password": "pwd",
                            "qq": "12312"
                        }
                    }
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    user_id = current_user.id
    users = UserService.query_user_all()

    # 过滤自己
    users.pop(user_id)

    if users:
        return make_api_response(payload=users)
    else:
        return make_api_response(message="用户不存在", statusCode=400)
