# -*- coding: utf-8 -*-
import logging

from flask import request
from flask_login import current_user, login_required

from bookStore import app
from bookStore.service.user.address import AddressInfoService
from bookStore.views.api import exports
from bookStore.views import make_api_response


@exports('/address/query', methods=['GET'])
@login_required
def query_address_info():
    """
    @api {GET} /address/query 查询用户收货地址信息
    @apiGroup Address
    @apiVersion 0.0.1
    @apiDescription 用于查询用户全部收货地址信息
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                   {
                        "status": "ok",
                        "payload":{
                            [
                                {
                                    'id': 123,
                                    'user_id': 1234,
                                    'name': 'name',
                                    'address': 'XX市XX区XX街道'
                                    'post_code': '100100',
                                    'phone': 123123124,
                                    'is_default': 0
                                },
                                {},
                                ...
                            ]
                        }
                    }
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    user_id = current_user.id
    if user_id:
        address_info_service = AddressInfoService()
        address_info_list = address_info_service.address_info_query(user_id=user_id)

        return make_api_response(payload=address_info_list)

    return make_api_response(message="用户不存在", statusCode=400)


@exports('/address/add', methods=['POST'])
@login_required
def add_address_info():
    """
    @api {POST} /address/add 增加收货地址信息
    @apiGroup Address
    @apiVersion 0.0.1
    @apiDescription 新增用户收货地址
    @apiParam {String} name 收货人姓名
    @apiParam {String} address 收货人地址
    @apiParam {int} post_code 邮编
    @apiParam {int} phone 联系电话
    @apiParamExample {json} 请求样例：
                    {
                        "name": "张三",
                        "address": "收货人地址",
                        "post_code": "邮编",
                        "phone": "联系电话"
                    }
    @apiSuccess (200) {String} msg 信息
    """
    user_id = current_user.id
    name = request.json['name']
    address = request.json['address']
    post_code = request.json['post_code']
    phone = request.json['phone']

    address_info_service = AddressInfoService()
    # 判断是否为第一条记录
    is_default = 0
    infos = address_info_service.address_info_query(user_id)
    if not infos:
        is_default = 1

    address_info = {
        'user_id': user_id,
        'name': name,
        'address': address,
        'post_code': post_code,
        'phone': phone,
        'is_default': is_default
    }

    rvs = address_info_service.address_add(address_info)

    return make_api_response()


@exports('/address/update', methods=['POST'])
@login_required
def update_address_info():
    """
    @api {POST} /address/update 修改收货地址信息
    @apiGroup Address
    @apiVersion 0.0.1
    @apiDescription 修改用户收货地址信息
    @apiParam {int} id 收货信息的编号
    @apiParam {String} name 收货人姓名
    @apiParam {String} address 收货人地址
    @apiParam {int} post_code 邮编
    @apiParam {int} phone 联系电话
    @apiParamExample {json} 请求样例：
                    {
                        "id": '123',
                        "name": "张三",
                        "address": "收货人地址",
                        "post_code": "邮编",
                        "phone": "联系电话"
                    }
    @apiSuccess (200) {String} msg 信息
    """
    user_id = current_user.id
    address_id = request.json['id']
    name = request.json['name']
    address = request.json['address']
    post_code = request.json['post_code']
    phone = request.json['phone']

    address_info = {
        'id': address_id,
        'user_id': user_id,
        'name': name,
        'address': address,
        'post_code': post_code,
        'phone': phone
    }
    address_info_service = AddressInfoService()
    rvs = address_info_service.address_update(address_info)

    return make_api_response()


@exports('/address/remove/<address_id>', methods=['GET'])
@login_required
def remove_address_info(address_id):
    """
    @api {GET} /address/remove/<address_id> 删除某条收货地址信息
    @apiGroup Address
    @apiVersion 0.0.1
    @apiDescription 删除某条收货地址信息
    @apiParam {int} id 收货信息的编号
    @apiSuccess (200) {String} msg 信息
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    user_id = current_user.id

    address_info_service = AddressInfoService()
    rvs = address_info_service.address_remove(address_id)

    if not rvs:
        return make_api_response(statusCode=400)

    return make_api_response()


@exports('/address/setdefault/<address_id>', methods=['GET'])
@login_required
def set_default_address_info(address_id):
    """
    @api {GET} /address/setdefault/<address_id> 设置默认收货地址
    @apiGroup Address
    @apiVersion 0.0.1
    @apiDescription 设置默认收货地址信息
    @apiParam {int} id 收货信息的编号
    @apiSuccess (200) {String} msg 信息
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    user_id = current_user.id
    address_info_service = AddressInfoService()
    rvs = address_info_service.address_set_default(user_id, address_id)

    if not rvs:
        return make_api_response(statusCode=400)

    return make_api_response()
