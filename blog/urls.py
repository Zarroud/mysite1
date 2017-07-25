from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from . import views
from blog.models import Post
from django.contrib.auth.decorators import login_required



urlpatterns=[  url(r'^comment/$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="blog/blog.html")),
               url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,template_name='blog/post.html')),		   
			   url(r'^blogForm/$',views.blogForm, name="blogForm"),
			   url(r'^savePost/$', views.savePost, name="contact"),
            ]
