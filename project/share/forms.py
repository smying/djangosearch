# -*- coding:utf-8 -*-
from django import forms
from django.core.validators import validate_email
from django.forms import ModelForm
from .models import Ebook, Type
#如果模型字段设置blank=True，那么表单字段的required 设置为False。否则，required=True。

class RegisterForm(forms.Form):
	username = forms.CharField(label="用户名:", max_length=100, required=True,  error_messages={'required': '请输入用户名'})#widget=forms.TextInput(attrs={'placeholder':u"用户名",})
	password = forms.CharField(label="密码:", error_messages={'required': u'请输入密码'}, widget=forms.PasswordInput())
	password2 = forms.CharField(label="确认密码:", error_messages={'required': u'请输入密码'}, widget=forms.PasswordInput())
	email = forms.EmailField()
	#recipients = MultiEmailField()
	#cc_myself = forms.BooleanField(required=False)
	#phone = forms.IntegerField()

class LoginForm(forms.Form):
	username = forms.CharField(label="用户名:", max_length=100, required=True,  error_messages={'required': '请输入用户名'})
	password = forms.CharField(label="密码:", error_messages={'required': u'请输入密码'}, widget=forms.PasswordInput())

class MultiEmailField(forms.Field):
	def to_python(self, value):
# Return an empty list if no input was given.
		if not value:
			return []
		return value.split(',')

	def validate(self, value):
		super(MultiEmailField, self).validate(value)

		for email in value:
			validate_email(email)

class ChangePasswordForm(forms.Form):
	oldpassword = forms.CharField(label="旧密码:", error_messages={'required': u'请输入密码'}, widget=forms.PasswordInput())
	password = forms.CharField(label="新密码:", error_messages={'required': u'请输入密码'}, widget=forms.PasswordInput())
	password2 = forms.CharField(label="确认密码:", error_messages={'required': u'请输入密码'}, widget=forms.PasswordInput())

class AuthorForm(forms.Form):
	realname = forms.CharField(label="真实姓名:", max_length=20,required=False)
	birth_date = forms.DateField(label="生日:", required=False)
	head = forms.ImageField(label="头像:", required=False)
	phone = forms.IntegerField(label="手机号码:", required=False)

class RecommendForm(forms.Form):
	name = forms.CharField(max_length=20)
	author = forms.CharField(max_length=30)
	brief = forms.CharField(max_length=200)
	pub_date = forms.DateField()
	types = forms.ModelChoiceField(queryset=Type.objects.all())
	pub_at = forms.CharField(max_length=15) 
	pic = forms.ImageField(label="图片:", required=False) 
	content = forms.CharField(widget=forms.Textarea())

class CommentForm(forms.Form):
	comments = forms.CharField(max_length=500)
	score = forms.FloatField(max_value=5.0, min_value=0.0)	

#widget=forms.CheckboxInput()
#if len(comments)>=20:count=True...

class AdviceForm(forms.Form):
	contents = forms.CharField(max_length=500)
	phone = forms.IntegerField()

class BbsForm(forms.Form):
	contents = forms.CharField(max_length=500)


'''如果模型字段设置了choices，那么表单字段的Widget 将设置成Select，其选项来自模型字段的choices。选项通常会包含空选项，并且会默认选择。如果字段是必选的，它会强制用户选择一个选项。如果模型字段的blank=False 且具有一个显示的default 值，将不会包含空选项（初始将选择default 值）

    title = forms.CharField(max_length=3,
                widget=forms.Select(choices=TITLE_CHOICES))


class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
class UserProfileForm(forms.ModelForm):
GENDER_CHOICES =(
(u'M',u'Male'),
(u'F',u'Female'),
)
gender = forms.ChoiceField(label=u'性别',choices=GENDER_CHOICES,
widget=forms.RadioSelect())
birthday = forms.DateField(required=True,widget=SelectDateWidget(years=range(1920,2030)),label='生日')
signature = forms.CharField(label=u'个性签名',widget=forms.Textarea({'size':10000}))
photo = forms.ImageField(label=u'上传你喜欢的头像')
class Meta:
model = UserProfile
exclude = ['user','usermail',]

'''
