from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, CustomUserCreationForm
from password.pwd import create_new_file


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/pwd/')
    else:
        if request.method == 'GET':
            login_form = UserLoginForm()
            signup_form = CustomUserCreationForm()
            return render(request, 'login.html', {'login': login_form, 'signup': signup_form})
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/pwd/')
            else:
                return redirect('/users/login')


def register_user(request):
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)
        pwd_db = request.POST['pwd_db']
        create_new_file(user.username, pwd_db)
        if user is not None:
            login(request, user)
            return redirect('/pwd/')
    else:
        return redirect('/users/login')


@login_required()
def logout_user(request):
    logout(request)
    return redirect('/users/login')
