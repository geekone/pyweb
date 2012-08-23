# -*- coding:utf-8

import os
import logging
import datetime

from logging.handlers import  RotatingFileHandler


from flask import Flask, g, session, request, flash, redirect, jsonify, url_for
from fkapp import views


#使用couchdb-ext
from flaskext.couchdb import CouchDBManager
from fkapp.models.model import User,Category,Shop

#关掉couchdbkit
#from fkapp.extensions import couchdb
#这里使用mongoalchemy
#from fkapp.extensions import db

DEFAULT_APP_NAME = 'fkapp'

DEFAULT_MODULES = (
    (views.frontend, ""),
    (views.admin, "/admin"),
 )

def create_app(config=None, modules=None):

    if modules is None:
        modules = DEFAULT_MODULES

    app = Flask(DEFAULT_APP_NAME)

    # config
    app.config.from_pyfile(config)

    #不在config文件中配置 mongoalchemy
#    app.config['MONGOALCHEMY_SERVER'] = '127.0.0.1'
#    app.config['MONGOALCHEMY_DATABASE'] = 'test'
#    app.config['MONGOALCHEMY_USER'] = 'ajaxj'
#    app.config['MONGOALCHEMY_PASSWORD'] = 'eeeeeeee'
    #这句关键，不设为false就账号通不过
#    app.config['MONGOALCHEMY_SERVER_AUTH'] = False

#    manager = CouchDBManager()
#    manager.add_document(User)
#    manager.add_document(Category)
#    manager.add_document(Shop)
#    manager.setup(app)

    #这句不解
#    manager.sync(app)
    #不写在配置文件中的方式
    #app.config['COUCHDB_DATABASE'] = 'mydb'




    #关掉couchdbkit或mongoalchemy
#    configure_extensions(app)

    configure_logging(app)

    # register module
    configure_modules(app, modules)

    return app



#关掉couchdbkit
#def configure_extensions(app):
#     # 关掉couchdb
#     couchdb.init_app(app)
    #使用mongoalchemy
#    db.init_app(app)





def configure_modules(app, modules):

    for module, url_prefix in modules:
        app.register_module(module, url_prefix=url_prefix)


def configure_logging(app):

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')

    debug_log = os.path.join(app.root_path,
        app.config['DEBUG_LOG'])

    debug_file_handler =\
    RotatingFileHandler(debug_log,
        maxBytes=100000,
        backupCount=10)

    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(formatter)
    app.logger.addHandler(debug_file_handler)

    error_log = os.path.join(app.root_path,
        app.config['ERROR_LOG'])

    error_file_handler =\
    RotatingFileHandler(error_log,
        maxBytes=100000,
        backupCount=10)

    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)
