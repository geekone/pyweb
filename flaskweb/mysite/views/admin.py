# -*- coding:utf-8 -*-
from mysite.models.model import Category,Item

from mysite.extensions import db
from mysite.utils.fetch import getCategory,getSubCategory,getItem


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
    _categorylist = Category.query.all()
    return render_template('admin/categorylist.html',categorylist = _categorylist)

#数据列表
@admin.route('/itemlist')
def itemlist():
    _itemlist = Item.query.all()
    return render_template('admin/itemlist.html',itemlist=_itemlist)


# 初始数据并首页跳转
@admin.route('/initdata')
def initdata():
    #添加分类
    _categoryList = getCategory()
    for _catename in _categoryList:
       _category = Category(name=_catename,subid = 1)
       db.session.add(_category)

    _sublist = getSubCategory()
    for _cate in _sublist:
        _category = Category(name=_cate[0],subid=_cate[1])
        db.session.add(_category)

    #取条目
    _itemList = getItem()
    for _title in _itemList:
        item = Item(title = _title,cateid = 77 )
        db.session.add(item)

    db.session.commit()
    return redirect(url_for('index'))


