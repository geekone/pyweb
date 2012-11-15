# -*- coding:utf-8 -*-
from mysite.models.model import Category,Item

from mysite.extensions import db

__author__ = 'window2003@gmail.com'


from flask import Module,redirect,url_for,render_template,current_app

__author__ = 'window2003@gmail.com'

admin = Module(__name__)

@admin.route('/')
def index():
    return render_template('admin/index.html')

#分类列表
@admin.route('/categorylist')
def categorylist():
#    print foo()
    #打印log
#    current_app.logger.debug("this is debug")
#    current_app.logger.error("this is error")
    _category = Category.query.all()
    print _category
    _item = Item.query.all()
    print _item
    return render_template('admin/categorylist.html')

#数据列表
@admin.route('/itemlist')
def itemlist():
    return render_template('admin/itemlist.html')


# 初始首页跳转
@admin.route('/initdata')
def initdata():
#    _category = Category(name="n1")
    _item = Item(title="t1")
#    db.session.add(_category)
    db.session.add(_item)
    db.session.commit()
    return redirect(url_for('index'))