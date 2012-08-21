# -*- coding:utf-8
from flaskext.couchdb import Document ,TextField,IntegerField


__author__ = 'window2003@gmail.com'



class User(Document):
    doc_type="user"
    username = TextField()
    password = TextField()
    nickname = TextField()
    level = IntegerField()



class Shop(Document):
    doc_type = "shop"
    title = TextField()
    addr = TextField()
    star = TextField()

