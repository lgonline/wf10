#!/usr/bin/env python
# encoding: utf-8

"""
@author: liugang9
@software: PyCharm
@file: __init__.py
@time: 2017/10/23 20:37
"""

from flask import Flask

app = Flask(__name__)

from app import views