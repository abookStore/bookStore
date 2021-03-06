# -*- coding:utf-8 -*-
from datetime import datetime
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

    def account_consume_add(self, user_id, consume, balance):
        """
        增加用户消费的记录
        """
        if not user_id or not consume:
            return None

        now = datetime.now()
        day = int(now.strftime('%Y%m%d'))
        month = int(now.strftime('%Y%m'))

        account_consume = AccountConsume()
        account_consume.user_id = user_id
        account_consume.amount = consume
        account_consume.current_balance = balance
        account_consume.day = day
        account_consume.month = month

        db.session.add(account_consume)
        db.session.flush()

        return True

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
            user_id=user_id).order_by(AccountRefund.id.desc()).all()

        return rows

    def account_change(self, user_id, change):
        """
        对余额进行扣款
        """
        if not change:
            return False

        sql = """
        UPDATE account SET
        balance = balance + :change
        WHERE user_id = :user_id
        LIMIT 1
        """

        return db.session.execute(sql, {'change': change, 'user_id': user_id}).rowcount

    def account_prepay(self, user_id, amount):
        """
        用户充值
        """
        if not amount:
            return False

        # 余额充值
        rowcount = self.account_change(user_id, amount)
        if rowcount < 0:
            return False

        # 记录充值log
        now = datetime.now()
        day = int(now.strftime('%Y%m%d'))
        month = int(now.strftime('%Y%m'))
        account = AccountService.account_query(user_id)
        balance = account['balance']

        prepay = AccountPrepay()
        prepay.user_id = user_id
        prepay.amount = amount
        prepay.current_balance = balance
        prepay.day = day
        prepay.month = month

        db.session.add(prepay)
        db.session.flush()

        return True
