# -*- coding:utf-8

from flaskext.wtf import Form,TextField,HiddenField,BooleanField,PasswordField,SubmitField,ValidationError,required,\
    email,equal_to,regexp


#用户登录的Form
class LoginForm(Form):
    username = TextField(u"用户名")
    password = PasswordField(u"密码")
    remember = BooleanField("Remember me")
    next = HiddenField()
    submit = SubmitField(u"登录")

#用户注册的Form
class SignupForm(Form):
	username = TextField(u"用户名",validators=[required(message=("username required"))])
	nickname = TextField(u"昵称",validators=[required(message=("nickname required"))])
	password = TextField(u"密码",validators=[required(message=("password required"))])
	next = HiddenField()
	submit = SubmitField(u"注册")
