# -*- coding: utf-8 -*-
import time
from bookStore import db, app

def run():
    while True:
        rv = sync_delivery_status()
        if rv is True:
            time.sleep(5)


def sync_delivery_status():
    """
    更新订单的送货状态
    """
    order_ids = get_order_id()
    order_ids = check_order_detail(order_ids)

    if order_ids:
        rv = update_delivery_status(order_ids)
        return rv

    return False

def get_order_id():
    """
    获取所有需要更新送货状态的订单id
    """
    sql = """
    SELECT
        order_id
    FROM `order`
    WHERE delivery_status = 0
    """

    rows = db.session.execute(sql).fetchall()

    return [row.order_id for row in rows]


def check_order_detail(order_ids):
    """
    核对订单详细信息中已发货的情况
    """
    sql = """
    SELECT
        order_id
    FROM (
        select
            order_id,
            sum(deliveried_quantity) sum_d
        from order_detail
        GROUP by order_id
    )o
    WHERE sum_d > 0
    AND order_id in :order_ids;
    """

    if not order_ids:
        return

    rows = db.session.execute(sql, {"order_ids": order_ids})

    return [row.order_id for row in rows]


def update_delivery_status(order_ids):
    """
    同步正在进行中的订单的送货状态
    """
    sql = """
    UPDATE `order` SET
        delivery_status = 1
    WHERE order_id in :order_ids
    """

    if not order_ids:
        return

    rowcount = db.session.execute(sql, {"order_ids": order_ids}).rowcount

    if rowcount > 0:
        db.session.commit()
        for order_id in order_ids:
            app.logger.info('同步配送状态完成 order_id: %s' % order_id)
        return True
    else:
        db.session.rollback()
        app.logger.info('同步配送状态失败')
        return False

