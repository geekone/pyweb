# -*- coding:utf-8 -*-
__author__ = 'window2003@gmail.com'


from flask import Module,redirect,url_for

__author__ = 'window2003@gmail.com'

admin = Module(__name__)

@admin.route('/')
def index():
    return "this is admin"

@admin.route('/categorylist')
def categorylist():
    return "this is category list"

@admin.route('/itemlist')
def itemlist():
    return "this is items list"