from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(UserCreationForm):
    title = forms.CharField(max_length=40, help_text='Required')
    body =  forms.CharField( widget=forms.Textarea )

    class Meta:
        model = User
        fields = ('title', 'body')
