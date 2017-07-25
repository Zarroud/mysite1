from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
	email = forms.EmailField(max_length=200, help_text='Required')
	first_name = forms.CharField(max_length=40, help_text='Required')
	last_name = forms.CharField(max_length=40, help_text='Required')

	class Meta:
		model = User
		fields = ('first_name', 'last_name' , 'username', 'email', 'password1', 'password2')


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	username = forms.CharField()

	class Meta:
		model = User
		fields = ['username','password']
		
		
class FindUserForm(forms.ModelForm):
	username = forms.CharField()

	class Meta:
		model = User
		fields = ['username']


class ContactForm(forms.ModelForm):
	from_email = forms.EmailField(max_length=200, help_text='Required')
	subject = forms.CharField(max_length=40, help_text='Required')
	message = forms.CharField( widget=forms.Textarea )


class Meta:
	model = User
	fields = ('subject', 'message', 'from_email')
		
		