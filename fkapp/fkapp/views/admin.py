# -*- coding:utf-8
from flask import Module,render_template,request,flash,redirect, current_app

#使用couchdb-ext
from fkapp.models.model import User,Shop,Category

#关掉couchdb-kit
#from fkapp.models.greeting import User

from fkapp.forms import LoginForm,SignupForm
from flaskext.couchdb import paginate



__author__ = 'Administrator'


admin = Module(__name__)

@admin.route("/")
def index():
#    current_app.logger.debug("loaded admin/index")
#    current_app.logger.error("this is error")
    return render_template('admin/index.html')


#分类
#所有分类
@admin.route("/categories/")
def categories():
    try:
        _category_results = Category.all()
    except Exception,e:
        current_app.logger.error(e);

    return render_template('admin/categories.html',categories=_category_results)

#添加分类
@admin.route('/categoryadd/')
def categoryadd():
    current_app.logger.error('this is category add page')
    return render_template('admin/categoryadd.html')

#删除分类
@admin.route('/categorydel/')
def categorydel():
    return redirect('admin/categories')


#Shop Bar

#Shop

@admin.route("/shops/")
def shops():
    try:
        _shop_results = Shop.all()
    except Exception,e:
        current_app.logger.error(e)

    return render_template('admin/shops.html',shops = _shop_results)

#跳转到添加页面
@admin.route('/shopadd/')
def shopadd():
    return render_template('admin/shopadd.html')

#删除
@admin.route('/shopdel')
def shopdel():
    return redirect('admin/shops')

#用户
@admin.route('/users/')
def users():
    try:
        _user_results = User.all()
    except Exception,e:
        current_app.logger.error(e)

    return render_template('admin/users.html',users = _user_results)

#添加
@admin.route('/useradd/')
def useradd():
    return render_template('admin/useradd.html')

#删除
@admin.route('/userdel/')
def userdel():
    return redirect('admin/users')



#@admin.route("/users",methods=('GET','POST'))
#def users():
#    if request.method == 'POST':
#        _username = request.form['username']
#        _password = request.form['password']
#        user = User(username=_username,password=_password)
#        user.save()
#        return render_template('admin/users1.html')
#    else:
#        return render_template('admin/users1.html')


@admin.route("/login/", methods=("GET","POST"))
def login():
    form = LoginForm(username=request.args.get('username',None),next=request.args.get('next',None))
    if form.validate_on_submit():
        flash("Welcome back, %s"% form.username.data, "success")
        next_url = form.next.data
        print next_url
        print form.username.data
        print form.password.data
        print form.remember.data
        return redirect('signup')


    return render_template('admin/login.html',form = form)



#user
@admin.route("/users1",methods=('GET','POST'))
def users1():
    form = SignupForm(next=request.args.get('next',None))
    if form.validate_on_submit():
        _username = form.username.data
        _password = form.password.data
        _nickname = form.nickname.data
        user = User(username=_username,password=_password,nickname = _nickname,level = 1)
        user.store()
        return redirect('admin/users1')
    else:
    #flash("back,errors")
        return render_template('admin/users1.html',form = form)




#注册用户
@admin.route("/signup/",methods=("GET","POST"))
def signup():
    form = SignupForm(next=request.args.get('next',None))
    if form.validate_on_submit():
        _username = form.username.data
        _password = form.password.data
        _nickname = form.nickname.data
        user = User(username=_username,password=_password,nickname = _nickname,level = 1)
        user.store()
        return redirect('/admin/users1')
    else:
    #flash("back,errors")
        return render_template('admin/signup.html',form = form)







#初始数据
@admin.route("/initdata")
def initdata():
    cate1 = Category(name='category1')
    cate1.store()
    cate2 = Category(name='category2')
    cate2.store()
    shop1 = Shop(title="shop1",addr="shop1 addr",star=1)
    shop1.store()
    shop2 = Shop(title="shop2",addr="shop2 addr",star=2)
    shop2.store()
    shop3 = Shop(title="shop3",addr="shop3 addr",star=3)
    shop3.store()

    user1 = User(username="test1",password="test1",nickname="Test1",level=0)
    user1.store()
    user2 = User(username="test2",password="test2",nickname="Test2",level=0)
    user2.store()
    user3 = User(username="test3",password="test3",nickname="Test3",level=0)
    user3.store()
    user4 = User(username="test4",password="test4",nickname="Test4",level=0)
    user4.store()


#    ls = Category.all()
#    for l in ls:
#        print l.name
#    page = paginate(Signature.all(), 5, request.args.get('start'))
#    print page
    return render_template('admin/shops.html')

