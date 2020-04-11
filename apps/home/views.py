# Django
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as LoginUser, logout as LogoutUser

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

    storage = get_messages(request)
    messages = []
    for m in storage:
        messages.append(m.message)
        print("Mensaje: ", m.message)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            LoginUser(request, user)
            print(username + ' y ' + password)
            return redirect('budget:panel')
        else:
            return render(
                request=request, 
                template_name='home/login.html',
                context={
                    "error": "Verifique sus datos de acceso"
                })

    return render(
        request=request,
        template_name='home/login.html',
        context={
            'messages':messages
        })

def signup(request):
    """ Signup client users"""
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['first_name']
            last_name = data['last_name']
            email = data['username']
            password1 = data['password1']
            password2 = data['password2']
            user = User.objects.create_user(
                username=email, email=email, password=password1)
            user.first_name = name
            user.last_name = last_name
            user.save()
            p = Profile(user=user)
            # is_client is True by defualt
            p.save()

            messages.success(request, 'Registro exitoso.')
            return redirect('home:login')

    return render(request, 'home/signup.html', {
        'form': form,
    })
