#!/usr/bin/env python
# encoding: utf-8

"""
@author: liugang9
@software: PyCharm
@file: views.py
@time: 2017/10/23 20:37
"""

from app import lm,db,oid,app
from flask import render_template,flash,redirect,url_for,session,g,request
from flask_login import login_user,logout_user,current_user,login_required
from .forms import LoginForm
from .models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    #user = {'nickname':'Peter'}
    user = g.user
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
    return render_template('index.html',title='Home',user=user,posts=posts)


@app.route('/login',methods=['GET','POST'])
#添加一个新的装饰器,告诉Flask-OpenID是的登录视图函数
@oid.loginhandler
def login():
    #检查g.use 是否被设置成一个认证用户，如果是的话将会被重定向到首页,g全局变量是一个在请求生命周期中用来存储和共享数据
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    #validate_on_submit 方法做了所有表单处理工作。当表单正在展示给用户的时候调用它，它会返回 False.
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        #oid.try_login被调用是为了触发用户使用Flask-OpenID认证
        return oid.try_login(form.openid.data,ask_for=['nickname','email'])
    #    flash('Login requested for OpenID="'+form.openid.data+'",remember_me'+str(form.remember_me.data))
    #    return redirect('/index')
    return render_template('login.html',title='Sign In',form=form,providers=app.config['OPENID_PROVIDERS'])

@lm.user_loader()
def load_user(id):
    #id发送给Flask-SQLAlchemy之前，必须把id转成整型，否则会报错！
    return User.query.get(int(id))

@oid.after_login()
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    #从数据库中搜索邮箱地址,如果邮箱地址不在数据库中，添加一个新用户到数据库。
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@'[0])
        user = User(nickname=nickname,email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me',None)
    #调用Flask-Login的login_use 函数注册这个有效的登录
    login_user(user,remember_me=remember_me)
    #在next页没有提供的情况下，会重定向到首页，否则会重定向到next页
    return redirect(request.args.get('next') or url_for('index'))

@app.before_request
def before_request():
    g.user = current_user


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
