# -*- coding:utf-8
from flaskext.couchdb import Document ,TextField,IntegerField, ViewField, ViewDefinition,DateTimeField

import datetime


__author__ = 'window2003@gmail.com'



# model
class Signature(Document):
    doc_type = 'signature'

    message = TextField()
    author = TextField()
    time = DateTimeField(default=datetime.datetime.now)

    all = ViewField('guestbook', '''
        function (doc) {
            if (doc.doc_type == 'signature') {
                emit(doc.time, doc);
            };
        }''')


class User(Document):
    doc_type="user"
    username = TextField()
    password = TextField()
    nickname = TextField()
    level = IntegerField()

    all = ViewField('blog', '''\
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

