# -*- coding:utf-8
__author__ = 'window2003@gmail.com'

#使用mongoalchemy
from fkapp.extensions import db

from flaskext.mongoalchemy import BaseQuery
import re

class BookQuery(BaseQuery):

    def starting_with(self, letter):
        regex = r'^' + letter
        return self.filter({'title' : re.compile(regex, re.IGNORECASE)})

class Book(db.Document):
    query_class = BookQuery
    title = db.StringField()
    year = db.IntField()


#关掉flask couchdbkit
# from fkapp.extensions import couchdb

# class Greeting(couchdb.Document):
#     author = couchdb.StringProperty()
#     content = couchdb.StringProperty()
#     date = couchdb.DateTimeProperty()


# # 用户
# class User(couchdb.Document):
#     username = couchdb.StringProperty()
#     password = couchdb.StringProperty()
#     nickname = couchdb.StringProperty()
#     create_at = couchdb.DateTimeProperty()


# # 比赛
# class Match(couchdb.Document):
#     host = couchdb.StringProperty()
#     guest = couchdb.StringProperty()



