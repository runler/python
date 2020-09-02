# pip install Flask-WTF
from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, HiddenField, DateField, DateTimeField, IntegerField, \
	DecimalField, FloatField, BooleanField, RadioField, SelectField, SelectMultipleField, FileField, SubmitField, \
	FormField, FieldList
from wtforms.validators import DataRequired, EqualTo, Length, NumberRange, URL, AnyOf, NoneOf

app = Flask(__name__)

app.config["SECRET_KEY"] = "AD2aafsdakflasf124f"


# 定义表单的模型类
class RegisterForm(FlaskForm):
	"""自定义注册表单模型类"""
	user_name = StringField(label='用户名：', validators=[DataRequired("用户名不能为空!")])
	password = PasswordField(label="密码：", validators=[DataRequired("密码不能为空！")])
	password2 = PasswordField(label="确认密码：", validators=[DataRequired("确认密码不能为空！"), EqualTo("password", "两次密码不一致！")])
	submit = SubmitField("提交")


@app.route("/register", methods=["GET", "POST"])
def register():
	# 创建表单对象,如果是post,表单值flask会在构造form对象时存放到对象中
	form = RegisterForm()
	#  验证form数据是否合理，成功返回真
	if form.validate_on_submit():
		uname = form.user_name.data
		psd = form.password.data
		psd2 = form.password2.data
		session["user_name"] = uname
		print(uname,psd,psd2)
		return redirect(url_for("index"))
	return render_template("register.html", form=form)


@app.route("/index")
def index():
	user_name = session.get("user_name", "")
	return "hello %s" % user_name


if __name__ == '__main__':
	app.run(Debug=True)