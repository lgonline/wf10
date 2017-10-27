#!/usr/bin/env python
# encoding: utf-8

"""
@author: liugang9
@software: PyCharm
@file: __init__.py
@time: 2017/10/23 20:37
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir
from app import models,views

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
#Flask-OpenID 扩展需要一个存储文件的临时文件夹的路径。对此，我们提供了一个 tmp 文件夹的路径。
oid = OpenID(app,os.path.join(basedir,'tmp'))
lm.login_view = 'login'
