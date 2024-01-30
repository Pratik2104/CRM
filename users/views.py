from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import *
from django.contrib.auth.decorators import *
from django.contrib.auth.models import Group
from accounts.models import *

# Create your views here.
@unauthenticated_user
def UserRegistration(request):
    register_form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if register_form.is_valid():
            user = register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request,"Registration Successful"+username)
            return redirect('login')
        else:
            messages.error(request,"Unsuccessful Registration! Please try again.")
    context = {
            'register_form' : register_form,
    }
    return render(request,'users/register.html',context)


@unauthenticated_user
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            messages.success(request,"Welcome "+username+". You have been Sucessfully logged in.")
            return redirect('home')
        else :
            messages.error(request,"Incorrect username or password! Try again.")
    return render(request,'users/login.html')

@login_required
def Logout(request):
    logout(request)
    messages.success(request,"Logged out!")
    return redirect('login')
