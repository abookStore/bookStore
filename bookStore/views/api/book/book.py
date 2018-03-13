# -*- coding: utf-8 -*-
from werkzeug.utils import secure_filename
from flask import request
from flask_login import current_user, login_required
from bookStore import app, db
from bookStore.mappings.book import Book
from bookStore.service.book.book import BookService
from bookStore.views.api import exports
from bookStore.views import make_api_response

ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])


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
                            "supplier": "天人1",
                            "discount": 0.5
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
        app.logger.info(rv)
        # 去除自己的书目
        if current_user.id and rv:
            for k, v in rv.copy().items():
                if str(current_user.id) == str(v.get('supplier_id')):
                    rv.pop(k)

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
                            "supplier": "天人1",
                            "discount": 0.5
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

        # 去除自己的书目
        if current_user.id:
            for k, v in rv.copy().items():
                if str(current_user.id) == str(v.get('supplier_id')):
                    rv.pop(k)

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
    discount = request.json['discount']

    book_info = {
        'isbn': isbn,
        'name': name,
        'author': author,
        'press': press,
        'quantity': quantity,
        'price': price,
        'description': description,
        'discount': discount
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
    user_id = current_user.id
    isbn = request.json['isbn']
    name = request.json['name']
    author = request.json['author']
    press = request.json['press']
    quantity = request.json['quantity']
    price = request.json['price']
    description = request.json['description']
    discount = request.json['discount']

    book_info = {
        'isbn': isbn,
        'name': name,
        'author': author,
        'press': press,
        'quantity': quantity,
        'price': price,
        'description': description,
        'discount': discount,
        'is_active': 1
    }
    book_service = BookService()
    rv = book_service.book_add(user_id, book_info)

    if rv:
        return make_api_response()
    else:
        return make_api_response(message='更新失败', statusCode=400)


@exports('/book/supplied', methods=['GET'])
@login_required
def book_supplied():
    """
    @api {GET} /book/supplied 当前用户书库中可提供的全部书目
    @apiGroup book
    @apiVersion 0.0.1
    @apiDescription 当前用户书库中可提供的全部书目
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
                            "supplier_id": 12,
                            "supplier": "天人1",
                            "discount": 0.4
                            }
                        },
                        "message": "ok"
                        }
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "缺少isbn"}
    """
    user_id = current_user.id
    if user_id:
        book_service = BookService()
        rv = book_service.books_query_by_supplier(user_id)

        return make_api_response(payload=rv, message='ok', statusCode=200)

    return make_api_response(message='用户不存在', statusCode=400)


@exports('/book/query_by_supplier_id/<supplier_id>', methods=['GET'])
@login_required
def book_query_by_supplier_id(supplier_id):
    """
    @api {GET} /book/query_by_supplier_id/<supplier_id> 根据用户id查询该书库中可提供的全部书目
    @apiGroup book
    @apiVersion 0.0.1
    @apiDescription 当前用户书库中可提供的全部书目
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
                            "supplier_id": 12,
                            "supplier": "天人1",
                            "discount": 0.4
                            }
                        },
                        "message": "ok"
                        }
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "缺少isbn"}
    """
    user_id = current_user.id
    if user_id:
        book_service = BookService()
        rv = book_service.books_query_by_supplier(supplier_id)

        return make_api_response(payload=rv, message='ok', statusCode=200)

    return make_api_response(message='用户不存在', statusCode=400)


@exports('/book/upload_by_excel', methods=['POST'])
@login_required
def book_upload_by_excel():
    """
    上传包含书目库存信息的excel
    @api {POST} /book/upload_by_excel 上传书目的 excel
    @apiGroup book
    @apiVersion 0.0.1
    @apiDescription 上传书目的 excel
    @apiParam {int} isbn
    @apiSuccess(200) {String} msg 信息
    """
    user_id = current_user.id

    if user_id:
        book_file = request.files.get('file', None)
        if book_file is None or not allowed_file(secure_filename(book_file.filename)):
            return make_api_response(message='文件不存在或类型有误', statusCode=400)

        # TODO
        # 遍历excel 存入db
        book_service = BookService()
        rv = book_service.add_books_by_excel(user_id, book_file)
        app.logger.info(rv)
        if rv:
            return make_api_response()

        return make_api_response(message='操作失败', statusCode=400)

    return make_api_response(message='用户不存在', statusCode=400)

# 用于判断文件后缀


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
