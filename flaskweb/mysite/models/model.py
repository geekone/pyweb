# -*- coding:utf-8 -*-
from mysite.extensions import db

__author__ = 'window2003@gmail.com'



class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    nickname = db.Column(db.String(50))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.email

    def __repr__(self):
        return "<%s>" % self.email

#分类模型
class Category(db.Model):
    __tablename__ = 'msg_category'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    subid = db.Column(db.Integer)

    def __repr__(self):
        return "<%s>" % self.name

#条目
class Item(db.Model):
    __tablename__='msg_item'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    cateid = db.Column(db.Integer)

    def __repr__(self):
        return "<%s>" % self.title





