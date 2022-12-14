from django.shortcuts import render, redirect
from django.http import FileResponse
from django.contrib.auth.decorators import login_required

from .pwd import *
from .forms import PasswordForm, GenerateForm


@login_required()
def open_db(request):
    user = request.user
    if request.method == 'GET':
        try:
            pwd_db = request.session['pwd_db']
            file = open_file(user=user, password=pwd_db)
            pwds = create_json(file)
            form = PasswordForm()
            user = request.user
            return render(request, 'pwd.html', {'file': pwds, 'form': form, 'user': user})
        except KeyError:
            return render(request, 'db_pwd.html')
    else:
        request.session['pwd_db'] = request.POST['password']
        return redirect('/pwd/')


@login_required()
def update_password(request):
    query = check_exists(request.POST['title'], user=request.user, pwd_db=request.session.get('pwd_db'))
    user = request.user
    pwd_db = request.session.get('pwd_db')
    title = request.POST['title'].capitalize()
    pwd = request.POST['password']
    password = check_pwd(pwd)
    username = request.POST['username']
    url = request.POST['url']
    if query:
        password_update(user=user, pwd_db=pwd_db, title=title, username=username, password=password, url=url)
    else:
        add_password(user=user, pwd_db=pwd_db, title=title, username=username, password=password, url=url)
    return redirect('/pwd/')


@login_required()
def del_password(request):
    user = request.user
    pwd_db = request.session.get('pwd_db')
    title = request.POST['title']
    delete_password(user=user, pwd_db=pwd_db, title=title)
    return redirect('/pwd/')


@login_required()
def generate_password(request):
    if request.method == 'GET':
        form = GenerateForm()
        return render(request, 'generate.html', {'form': form})
    else:
        form = GenerateForm(request.POST)
        length = request.POST['length']
        option = request.POST['option']
        pwd = random_pwd(length=length, option=option)
        return render(request, 'generate.html', {'pwd': pwd, 'form': form})


@login_required()
def download(request):
    user = request.user
    filename = f"{path}/{user}.kdbx"
    response = FileResponse(open(filename, 'rb'))
    return response
