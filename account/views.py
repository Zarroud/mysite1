from builtins import OverflowError, TypeError, ValueError, len
from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth import login as log, authenticate 
from .forms import SignupForm, UserForm, FindUserForm, ContactForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.core import mail
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.contrib import auth, messages
from django.template.context_processors import csrf
from django.views.generic.edit import FormView
from django.views.generic import View
from . import views
from account.models import EmailConfirmation
from smtplib import SMTP
from django.conf.urls import url, include



def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		strRetour = 'problem in form'
		if form.is_valid():
			try:
				user = form.save(commit = False)
				user.is_active = False
				user.save()
				current_site = get_current_site(request)
				subject = 'Activate your blog account.'
				message = render_to_string('account/acc_active_email.html', {
				'user':user, 'domain':current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
				})
				# user.email_user(subject, message)
				toemail = form.cleaned_data.get('email')
				email = EmailMessage(subject, message, to=[toemail])
				email.send()
				print ('successfuly sent')
				print("user info name : ", user.username, "user info id : ", user.id, "user info status : " , user.is_active)
				e=EmailConfirmation(user=user , status="sent")
				e.save()
				strRetour="Please confirm your email address to complete the registration"
			except:
				print ("not sent")
				print ("user info name : ", user.username, "user info id : ", user.id, "user info status : " , user.is_active)
				e=EmailConfirmation(user=user , status="not sent")
				e.save()
				strRetour="email was not sent, but your account was created and contact the admin on the contact page to active it"
			return HttpResponse(strRetour)
		else:
			return HttpResponse(strRetour)
	else:
		form = SignupForm()
	return render(request, 'account/signup.html', {'form': form})



@user_passes_test(lambda u: u.is_superuser)
def monitorUsers(request):
	return render(request, 'account/monitorUsers.html', {'users': EmailConfirmation.objects.all().order_by("user__id")})


def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		log(request, user)
		# return redirect('home')
		return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
	else:
		return HttpResponse('Activation link is invalid!')


def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('account/login.html', c)


def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/account/loggedin')
	else:
		return HttpResponseRedirect('/account/invalid')


@login_required
def loggedin(request):
	return render(request, 'account/loggedin.html', {'full_name': request.user.username})


def invalid(request):
	return render_to_response('account/invalid.html')


def logout(request):
	auth.logout(request)
	return render_to_response('account/logout.html')


@user_passes_test(lambda u: u.is_superuser)
def del_user(request, pk):
	u = get_object_or_404(User, id=pk)
	# User.objects.get(pk = id)
	u.delete()
	return redirect('/account/monitorUsers')


@user_passes_test(lambda u: u.is_superuser)
def activate_user(request, pk):
	# u = get_object_or_404(User, id=pk)
	u = User.objects.get(id=pk)
	u.is_active = True
	u.save()
	# User.objects.get(pk = id)
	# u.update(is_active=True)
	return redirect('/account/monitorUsers')


@user_passes_test(lambda u: u.is_superuser)
def desactivate_user(request, pk):
	u = User.objects.get(id=pk)
	u.is_active = False
	u.save()
	# User.objects.get(pk = id)
	# u.update(is_active=True)
	return redirect('/account/monitorUsers')


@user_passes_test(lambda u: u.is_superuser)
def find_user(request):
	try:
		username = request.GET.get('username')
		# u=table.objects.filter(username__contains=username)
		# User.objects.get(pk = id)
		# u.update(is_active=True)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		username = None
	if username is not None:
		return render(request, 'account/monitorUsers.html', {'users': EmailConfirmation.objects.filter(user__username__contains=username)})
				
	else:
		return redirect('/account/monitorUsers')


def listEmailConf(request):
	 q = EmailConfirmation.objects.all()
	 return render(request, 'account/testhtml.html', {'email': q})


def contact(request):
	return render(request, 'account/contact.html')


def	contactBymail(request):
	subject = request.POST.get('subject', '')
	message = request.POST.get('message', '')
	from_email = request.POST.get('from_email', '')
	if subject and message and from_email:
		try:
			send_mail(subject, message, from_email, ['y.zarroud@enim.ac.ma'])
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		return HttpResponseRedirect('/account/contact/')
	else:
		# In reality we'd use a form class
		# to get proper validation errors.
		return HttpResponse('Make sure all fields are entered and valid.')










