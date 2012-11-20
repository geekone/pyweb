__author__ = 'Administrator'

from flask import Flask
from flaskext.mongoalchemy import MongoAlchemy
app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'library'
db = MongoAlchemy(app)

class Category(db.Document):
    name = db.StringField()

class Item(db.Document):
    content = db.StringField()
    category = db.DocumentField(Category)



@app.route("/")
def index():
    category1 = Category(name="category1")
    item1 = Item(content="item1 title",category=category1)
    category1.save()
    item1.save()
    return "Msg home"

@app.route('/initdata')
def initdata():
    category = Category(name="category1")
    category.save()
    category = Category(name="category2")
    category.save()
    category = Category(name="category3")
    category.save()
    return "init data"


@app.route("/test")
def test():
    #查找修改保存
    _category = Category.query.filter(Category.name == 'category1').first()
    print _category
    print _category.name
    _category.name = "abcd"
    _category.save()
    return "this is test"

@app.route('/test1')
def test1():
    #TODO _category = Category.query.filter()
    return "this is test1"

if __name__ == "__main__":
    app.run()