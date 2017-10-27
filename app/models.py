#!/usr/bin/env python
# encoding: utf-8

"""
@author: liugang9
@software: PyCharm
@file: models.py
@time: 2017/10/26 16:16
"""

from app import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nickname = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(128),index=True,unique=True)
    posts = db.relationship('Post',backref='author',lazy='dynamic')

    #除非表示用户的对象因为某些原因不允许被认证。
    def is_authenticated(self):
        return True

    #除非是用户是无效的，比如因为他们的账号是被禁止。
    def is_active(self):
        return True

    #除非是伪造的用户不允许登录系统。
    def is_anonymous(self):
        return False

    #返回一个用户唯一的标识符，unicode格式。Python2和3对unicode处理的方式不同
    def get_id(self):
        try:
            return unicode(self.id)#python 2
        except NameError:
            return str(self.id)#python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DATETIME)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)