from builtins import OverflowError, TypeError, ValueError, len
from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, render_to_response 
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from blog.models import Post


#this function returns a blog form
@login_required
def blogForm(request):
	return render(request,'blog/blogForm.html',{'full_name': request.user.username})

#this function is for creating posts	
@login_required
def savePost(request):
	title=request.POST.get("title" , "")
	body=request.POST.get("body" , "")
	user=request.user	
	if body and title :
		try:
			post=Post(publisher=user , body=body , title=title)
			post.save
		except:
			return HttpResponse('you have an error.')
		return HttpResponseRedirect('/blog/blogForm/')
	else:
		# In reality we'd use a form class
		# to get proper validation errors.
		return HttpResponse('make sure that your body and title are not empty.')
		
	
