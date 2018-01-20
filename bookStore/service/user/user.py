# -*- coding: utf-8 -*-
from bookStore import db
from bookStore.mappings.user import User
class UserService():

    @staticmethod
    def query_user(username=None):
        """
        根据用户昵称查询

        Returns:
            account 不存在时返回 None
        """
        payload = {}
        if username:
            rv = db.session.query(User).filter_by(
                username=username).first()
            payload['username'] = rv['username']
            payload['nickname'] = rv['nickname']
            payload['realname'] = rv['realname']
            payload['password'] = rv['password']
            payload['phone'] = rv['phone']
            payload['gender'] = rv['gender']
            payload['mail'] = rv['mail']
            payload['qq'] = rv['qq']

            return payload

        raise NotImplementedError('不支持的查询方式')

    @staticmethod
    def create_user(userinfo):
        """
        创建新用户
        """
        user = User()
        user.username = userinfo['username']
        user.nickname = userinfo['nickname']
        user.realname = userinfo['realname']
        user.password = userinfo['password']
        user.phone = userinfo['phone']
        user.question = userinfo['question']
        user.answer = userinfo['answer']
        user.gender = userinfo['gender']
        user.mail = userinfo['mail']
        user.qq = userinfo['qq']

        db.session.add(user)
        db.session.flush()

        return True

    @staticmethod
    def get(id):
        user = User.query.filter_by(id=id).first()
        return SiteUser(user)

    @staticmethod
    def login(username, password):

        def md5(_):
            m = hashlib.md5()
            m.update(_.encode('utf-8'))
            return m.hexdigest()

        password = md5(md5(password))
        app.logger.info(password)

        user = User.query.filter_by(
            username=username, password=password).first()
        return (user is not None, SiteUser(user))

    @staticmethod
    def get_usernames(user_ids):
        rows = db.session.query(User).\
            filter(User.id.in_(list(user_ids))).\
            all()
        return {row.id: row.username for row in rows}

    @staticmethod
    def update_userinfo(userinfo):
        username = userinfo['username']
        if username:
            rv = db.session.query(User).filter_by(
                username=username).first()
            if rv:
                rv.nickname = userinfo['nickname']
                rv.realname = userinfo['realname']
                rv.gender = userinfo['gender']
                rv.mail = userinfo['mail']
                rv.phone = userinfo['phone']
                rv.qq = userinfo['qq']

                db.session.commit()