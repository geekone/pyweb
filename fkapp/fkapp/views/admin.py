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
    current_app.logger.debug("loaded admin/index")
    current_app.logger.error("this is error")
    return render_template('admin/index.html')


#分类
#所有分类
@admin.route("/categories/")
def categories():
    try:
        results = Category.all()
    except Exception,e:
        current_app.logger.error(e);

    return render_template('admin/categories.html',categories=results)

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
    return render_template('admin/shops.html')

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
    return render_template('admin/users.html')

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
#        return render_template('admin/users.html')
#    else:
#        return render_template('admin/users.html')


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



##user
#@admin.route("/users",methods=('GET','POST'))
#def users():
#    form = SignupForm(next=request.args.get('next',None))
#    if form.validate_on_submit():
#        _username = form.username.data
#        _password = form.password.data
#        _nickname = form.nickname.data
#        user = User(username=_username,password=_password,nickname = _nickname,level = 1)
#        user.store()
#        return redirect('admin/users')
#    else:
#    #flash("back,errors")
#        return render_template('admin/users.html',form = form)




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
        return redirect('/admin/users')
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
#    ls = Category.all()
#    for l in ls:
#        print l.name
#    page = paginate(Signature.all(), 5, request.args.get('start'))
#    print page
    return render_template('admin/shops.html')

