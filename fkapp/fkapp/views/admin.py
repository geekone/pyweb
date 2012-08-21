# -*- coding:utf-8
from flask import Module,render_template,request,flash,redirect

#使用couchdb-ext
from fkapp.models.model import User,Shop,Signature

#关掉couchdb-kit
#from fkapp.models.greeting import User

from fkapp.forms import LoginForm,SignupForm
from flaskext.couchdb import paginate


__author__ = 'Administrator'


admin = Module(__name__)

@admin.route("/")
def index():
    return render_template('admin/index.html')

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



#user
@admin.route("/users",methods=('GET','POST'))
def users():
    form = SignupForm(next=request.args.get('next',None))
    if form.validate_on_submit():
        _username = form.username.data
        _password = form.password.data
        _nickname = form.nickname.data
        user = User(username=_username,password=_password,nickname = _nickname,level = 1)
        user.store()
        return redirect('admin/users')
    else:
    #flash("back,errors")
        return render_template('admin/users.html',form = form)




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



#Shop

@admin.route("/shops/")
def shops():
    return render_template('admin/shops.html')


@admin.route("/test")
def test():
    signature = Signature(message='message', author='author')
    signature.store()
    print Signature.all()
#    page = paginate(Signature.all(), 5, request.args.get('start'))
#    print page
    return render_template('admin/shops.html')

