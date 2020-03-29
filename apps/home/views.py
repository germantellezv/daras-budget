# Django
from django.shortcuts import render, redirect
from django.contrib.auth import login as LoginUser, logout as LogoutUser
from django.contrib.auth import authenticate

# Decorators
from django.contrib.auth.decorators import login_required

# Forms
from .forms import SignUpForm
from django import forms

# Models
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.

@login_required
def logout(request):
    LogoutUser(request)
    return redirect('home:login')

def login(request):
    """ Login view """

    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = authenticate(request, username=username, password=password)
       if user:
           LoginUser(request, user)
           print(username + ' y ' + password)
           return redirect('budget:choose')
       else:
           return render(request, 'home/login.html', {"error": "Verifique sus datos de acceso"})

    return render(request, 'home/login.html')

def signup(request):
    """ Signup view """
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data['username']
            password1 = data['password1']
            password2 = data['password2']

            user = User.objects.create_user(username=email, email=email, password=password1)
            p = Profile(user = user)
            p.save()

            return redirect('home:login')

    return render(request,'home/signup.html',{
        'form':form,
    })
