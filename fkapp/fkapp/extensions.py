# -*- coding:utf-8
from flaskext.mongoalchemy import MongoAlchemy

__author__ = 'window2003@gmail.com'
#关闭 flask couchdbkit
# from flaskext.couchdbkit import CouchDBKit

# __all__=['couchdb']

# couchdb = CouchDBKit()

#使用 mongoalchemy
_all_ = ['db']

db = MongoAlchemy()
