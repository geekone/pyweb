# -*- coding:utf-8
import datetime
from flask import Module,render_template

# 停止couchdbkit
# from fkapp.models.greeting import Greeting
from fkapp.models.greeting import Book

__author__ = 'Administrator'


frontend = Module(__name__)

@frontend.route("/")
def index():
    # greet = Greeting(
    #     author="Benoit1111",
    #     content="Welcome to couchdbkit world",
    #     date=datetime.datetime.utcnow()
    # )
    # greet.save()
    return render_template('index.html')


@frontend.route("/backbonetest")
def backbonetest():
    return render_template("backbonetest.html")

@frontend.route('/testmongo')
def testmongo():
    dive = Book(title='Dive Into Python', year=2004)
    dive.save()
    return  "testmongo"