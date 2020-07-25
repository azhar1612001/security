from django.shortcuts import render
from django.http import HttpResponse
from .models import BookingDetail
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import *
from .forms import *

def home(request):
	return render(request,'aj/home.html')

def about(request):
	return render(request,'aj/about.html')

def packages(request):
	return render(request,'aj/packages.html')

def services(request):
	return render(request,'aj/services.html')

def center(request):
	return render(request,'aj/center.html')

def review(request):
	return render(request,'aj/review.html')

def gallary(request):
	return render(request,'aj/gallary.html')

def book(request):
	return render(request,'aj/book.html')

def bookDetail(request):
	if request.method=='POST':
		detail=BookingDetail()
		detail.name=request.POST['name']
		detail.phone=request.POST['phone']
		detail.date=request.POST['date']
		detail.address=request.POST['address']
		detail.city=request.POST['city']
		detail.state=request.POST['state']
		detail.pin_code=request.POST['pin_code']
		if not request.POST['message']=="":
			detail.message=request.POST['message']
		detail.save()
	return render(request,'aj/confirm.html')

def login(request):
	context={}
	return render(request,'aj/login.html',context)

def register(request):
	form=CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
	context={'form':form}
	return render(request,'aj/register.html',context)

def superuser(reuest):
	return render(request,'superuser.html')