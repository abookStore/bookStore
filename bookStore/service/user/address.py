# -*- coding:utf-8 -*-

from bookStore import db, app
from bookStore.mappings.address_info import AddressInfo

class AddressInfoService():
    def address_info_query(self, user_id):
        """
        查询收货地址的信息
        """
        address_info_list = []
        if user_id:
            rows = db.session.query(AddressInfo).filter_by(
                user_id=user_id).all()

            if rows:
                for row in rows:
                    address_info = {}
                    address_info['id'] = row.id
                    address_info['user_id'] = row.user_id
                    address_info['name'] = row.name
                    address_info['address'] = row.address
                    address_info['post_code'] = row.post_code
                    address_info['phone'] = row.phone
                    address_info['is_default'] = row.is_default

                    address_info_list.append(address_info)

            return address_info_list

        return None

    def address_query_by_id(self, user_id, address_id):
        """
        查询最早的默认收货地址记录
        """
        row = db.session.query(AddressInfo).filter_by(
            user_id=user_id, id=address_id).first()

        return row

    def address_add(self, address_info):
        """
        新增收货地址
        """
        if address_info:
            info = AddressInfo()
            info.user_id = address_info.get('user_id')
            info.name = address_info.get('name')
            info.address = address_info.get('address')
            info.post_code = address_info.get('post_code')
            info.phone = address_info.get('phone')
            info.is_default = address_info.get('is_default')

            db.session.add(info)
            db.session.flush()
            db.session.commit()

            return True

        return False

    def address_update(self, address_info):
        """
        更新收货地址
        """
        if address_info:
            info_id = address_info.get('id')
            info = db.session.query(AddressInfo).filter_by(
                id=info_id).first()

            info.user_id = address_info.get('user_id')
            info.name = address_info.get('name')
            info.address = address_info.get('address')
            info.post_code = address_info.get('post_code')
            info.phone = address_info.get('phone')

            db.session.flush()
            db.session.commit()

            return True
        return False

    def address_remove(self, user_id, address_id):
        """
        删除指定收货地址
        """
        sql = """
        DELETE FROM address_info
        WHERE id = :id
        LIMIT 1;
        """
        if address_id:
            db.session.execute(sql, {'id': address_id})

            # 如果删除的是默认地址，则分配新的默认地址
            default = self.get_default_address_query(user_id)

            if not default:
                old = self.get_oldest_address(user_id)
                if old:
                    self.address_set_default(user_id, old.id)

                    return True

        return False

    def address_set_default(self, user_id, address_id):
        """
        指定默认收货地址
        """
        # 取消当前默认地址
        sql_cancel = """
        UPDATE address_info
        SET is_default = 0
        WHERE user_id = :user_id
        AND is_default = 1
        LIMIT 1;
        """

        # 设置新的默认地址
        sql_set = """
        UPDATE address_info
        SET is_default = 1
        WHERE id = :id
        AND is_default = 0
        LIMIT 1;
        """
        if address_id:
            db.session.execute(sql_cancel, {'user_id': user_id})
            db.session.execute(sql_set, {'id': address_id})
            db.session.commit()

            return True

        return False

    def get_default_address_query(self, user_id):
        """
        查询是否存在默认收货地址
        """
        row = db.session.query(AddressInfo).filter_by(
            user_id=user_id, is_default=1).first()

        if row:
            return True

        return False
    
    def get_oldest_address(self, user_id):
        """
        查询最早的默认收货地址记录
        """
        row = db.session.query(AddressInfo).filter_by(
            user_id=user_id).order_by(AddressInfo.id.asc()).first()

        return row


