# -*- coding: utf-8 -*-

from flask import request
from flask_login import current_user, login_required
from bookStore.mappings.book import Book
from bookStore.service.book.book import BookService
from bookStore.views.api import exports
from bookStore.views import make_api_response

@exports('/book/query_by_isbn/<isbn>', methods=['GET'])
# @login_required
def query_book_by_isbn(isbn):
    """
    @api {GET} /book/query_book_by_isbn/<isbn> 根据 isbn 查询书目信息
    @apiGroup book
    @apiVersion 0.0.1
    @apiDescription 根据 isbn 查询书目信息
    @apiParam {int} isbn
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                        {
                        "status": "ok",
                        "payload": {
                            "1": {
                            "name": "论语", 
                            "press": "北京教育出版社", 
                            "id": 1, 
                            "description": null, 
                            "quantity": 100, 
                            "price": 0.0, 
                            "author": "周杰伦", 
                            "isbn": 9203204223,
                            "supplier": "天人1"
                            }
                        }, 
                        "message": "ok"
                        }
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "缺少isbn"}
    """
    if isbn:
        book_service = BookService()
        rv = book_service.book_query_by_isbn(isbn)

        return make_api_response(payload=rv, message='ok', statusCode=200)
    
    return make_api_response(message='缺少isbn')


@exports('/book/query_by_name/<name>', methods=['GET'])
# @login_required
def query_book_by_name(name):
    """
    @api {GET} /book/query_book_by_name/<name> 根据 书名 查询书目信息
    @apiGroup book
    @apiVersion 0.0.1
    @apiDescription 根据 书名 查询书目信息
    @apiParam {string} name 书名
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                        {
                        "status": "ok",
                        "payload": {
                            "1": {
                            "name": "论语", 
                            "press": "北京教育出版社", 
                            "id": 1, 
                            "description": null, 
                            "quantity": 100, 
                            "price": 0.0, 
                            "author": "周杰伦", 
                            "isbn": 9203204223,
                            "supplier": "天人1"
                            }
                        }, 
                        "message": "ok"
                        }
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "缺少isbn"}
    """
    if name:
        book_service = BookService()
        rv = book_service.book_query_by_name(name)

        return make_api_response(payload=rv, message='ok', statusCode=200)

    return make_api_response(message='缺少isbn')


@exports('/book/remove/<book_id>', methods=['GET'])
@login_required
def book_remove(book_id):
    """
    根据 id 删除书目信息
    """
    if book_id:
        book_sevice = BookService()
        rs = book_sevice.book_remove(book_id)
        if rs:
            return make_api_response()
        else:
            return make_api_response('操作失败')
    return make_api_response(message='缺少书目id')

@exports('/book/update', methods=['POST'])
@login_required
def book_update():
    """
    更新书目信息
    """
    book_id = request.json['id']
    isbn = request.json['isbn']
    name = request.json['name']
    author = request.json['author']
    press = request.json['press']
    quantity = request.json['quantity']
    price = request.json['price']
    description = request.json['description']

    book_info = {
        'isbn': isbn,
        'name': name,
        'author': author,
        'press': press,
        'quantity': quantity,
        'price': price,
        'description': description
    }
    book_service = BookService()
    rv = book_service.book_update(book_id, book_info)

    if rv:
        return make_api_response()
    else:
        return make_api_response(message='更新失败', statusCode=400)


@exports('/book/add', methods=['POST'])
@login_required
def book_add():
    """
    更新书目信息
    """
    isbn = request.json['isbn']
    name = request.json['name']
    author = request.json['author']
    press = request.json['press']
    quantity = request.json['quantity']
    price = request.json['price']
    description = request.json['description']

    book_info = {
        'isbn': isbn,
        'name': name,
        'author': author,
        'press': press,
        'quantity': quantity,
        'price': price,
        'description': description,
        'is_active': 1
    }
    book_service = BookService()
    rv = book_service.book_add(book_info)

    if rv:
        return make_api_response()
    else:
        return make_api_response(message='更新失败', statusCode=400)
