#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: lgonline 
@license: Apache Licence  
@contact: lgonline@hotmail.com 
@site:  
@software: PyCharm 
@file: forms.py 
@time: 10/23/17 11:51 PM 
"""

from flask_wtf import Form
from wtforms import StringField,BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid',validators=[DataRequired()])
    remember_me = BooleanField('remember_me',default=False)

def func():
    pass


class main():
    def __init__(self):
        pass


if __name__ == "__main__":
    main()
    pass  