#!/usr/bin/env python
# encoding: utf-8

"""
@author: liugang9
@software: PyCharm
@file: views.py
@time: 2017/10/23 20:37
"""

from app import app
from flask import render_template,flash,redirect
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Peter'}
    posts = [
        {
            'author':{'nickname':'John'},
            'body':'Beautiful day in portland'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',user=user,posts=posts)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    #validate_on_submit 方法做了所有表单处理工作。当表单正在展示给用户的时候调用它，它会返回 False.
    if form.validate_on_submit():
        flash('Login requested for OpenID="'+form.openid.data+'",remember_me'+str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='Sign In',form=form,providers=app.config['OPENID_PROVIDERS'])