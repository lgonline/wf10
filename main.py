#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: lgonline 
@license: Apache Licence  
@contact: lgonline@hotmail.com 
@site:  
@software: PyCharm 
@file: main.py 
@time: 10/24/17 10:35 PM 
"""

from flask import Flask
from apps_config import DevConfig

myapps = Flask(__name__)
myapps.config.from_object(DevConfig)

@myapps.route('/')
def home():
    return '<h1>Hello World!!!</h1>'


if __name__ == "__main__":
    myapps.run()
    pass  