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

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DATETIME)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)