# -*- coding:utf-8
from flaskext.couchdb import Document ,TextField,IntegerField, ViewField, ViewDefinition,DateTimeField

import datetime


__author__ = 'window2003@gmail.com'



# model
class Category(Document):
    doc_type = 'category'
    name = TextField()

    all = ViewField('category', '''
        function (doc) {
            if (doc.doc_type == 'category') {
                emit(doc._id, doc);
            };
        }''')

class User(Document):
    doc_type="user"
    username = TextField()
    password = TextField()
    nickname = TextField()
    level = IntegerField()
    create_at = DateTimeField(default=datetime.datetime.now)
    all = ViewField('user', '''\
    function (doc) {
        if (doc.doc_type == 'user') {
                emit(null, doc);
        };
    }''')



class Shop(Document):
    doc_type = "shop"
    title = TextField()
    addr = TextField()
    star = TextField()

