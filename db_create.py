#!/usr/bin/env python
# encoding: utf-8

"""
@author: liugang9
@software: PyCharm
@file: db_create.py
@time: 2017/10/26 16:22
"""

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import  SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path
db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO,'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)