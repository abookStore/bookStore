# -*- coding:utf-8 -*-

from bookStore import db, app
from bookStore.mappings.account import Account
from bookStore.mappings.account_consume import AccountConsume
from bookStore.mappings.account_prepay import AccountPrepay
from bookStore.mappings.account_refund import AccountRefund

class AccountService():
    @staticmethod
    def account_query(user_id):
        """
        查询用户账户相关的信息
        """
        payload = {}
        if user_id:
            account = db.session.query(Account).filter_by(user_id=user_id).first()

            if account:
                payload['user_id'] = account.user_id
                payload['balance'] = float(account.balance)
                payload['bonus_point'] = account.bonus_point
                payload['discount'] = float(account.discount)

            return payload

        return None

    def account_log_query(self, user_id):
        """
        查询用户所有消费行为的最近记录
        """
        if not user_id:
            return None

        sql = """
        select
            *
        from
        (
            select
                user_id,
                amount,
                current_balance,
                '余额消费' as t,
                created_at
            from account_consume a
            where user_id = :user_id

            union all

            select
                user_id,
                amount,
                current_balance,
                '充值' as t,
                created_at
            from account_prepay b
            where user_id = :user_id

            union all

            select
                user_id,
                amount,
                current_balance,
                '退款' as t,
                created_at
            from account_refund c
            where user_id = :user_id
        ) `all`
        order by created_at desc
        limit 10
        """
        rows = db.session.execute(sql, {"user_id": user_id}).fetchall()

        rvs = {}
        for row in rows:
            rv = {}
            rv['user_id'] = row.user_id
            rv['amount'] = float(row.amount)
            rv['current_balance'] = float(row.current_balance)
            rv['type'] = row.t
            created_at = row.created_at.strftime('%Y-%m-%d %H:%M:%S')
            rv['created_at'] = created_at
            rvs[created_at] = rv
        return rvs

    def account_consume_query(self, user_id):
        """
        查询用户消费相关的记录
        """
        if not user_id:
            return None

        rows = db.session.query(AccountConsume).filter_by(
            user_id=user_id).order_by(AccountConsume.id.desc()).all()

        return rows

    def account_prepay_query(self, user_id):
        """
        查询用户充值相关的记录
        """
        if not user_id:
            return None

        rows = db.session.query(AccountPrepay).filter_by(
            user_id=user_id).order_by(AccountPrepay.id.desc()).all()

        return rows

    def account_refund_query(self, user_id):
        """
        查询用户退款相关的记录
        """
        if not user_id:
            return None

        rows = db.session.query(AccountRefund).filter_by(
            user_id=user_id).order_by(AccountRefund.id.desc()) .all()

        return rows
