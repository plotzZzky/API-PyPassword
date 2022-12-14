from pathlib import Path

from pykeepass import PyKeePass, create_database
import random
import string
import json

path = Path('password/files/').absolute()


def create_new_file(user, password):
    file = f"{path}/{user}.kdbx"
    db = create_database(filename=file, password=password)
    return db


def open_file(user, password):
    try:
        file = f"{path}/{user}.kdbx"
        pyk = PyKeePass(filename=file, password=password)
        return pyk
    except FileNotFoundError:
        return False


def change_file_password(user, pwd_db, password):
    pyk = open_file(user, pwd_db)
    pyk.password = password
    pyk.save()


def add_password(user, pwd_db, title, username, password, url):
    pyk = open_file(user, pwd_db)
    pyk.add_entry(title=title, username=username, password=password, url=url, destination_group=pyk.root_group)
    pyk.save()


def password_update(user, pwd_db, title, username, password, url):
    pyk = open_file(user, pwd_db)
    entry = pyk.find_entries(title=title, first=True)
    entry.title = title
    entry.username = username
    entry.password = password
    entry.url = url
    pyk.save()


def delete_password(user, pwd_db, title):
    pyk = open_file(user, pwd_db)
    entry = pyk.find_entries(title=title, first=True)
    pyk.delete_entry(entry=entry)
    pyk.save()


def random_pwd(length, option):
    characters = None
    amount = int(length)
    char_option = int(option)
    match char_option:
        case 1:
            characters = string.ascii_letters
        case 2:
            characters = string.ascii_letters + string.digits
        case 3:
            characters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(characters) for i in range(amount))
    return result_str


def check_exists(new_name, user, pwd_db):
    pyk = open_file(user, pwd_db)
    entries = pyk.entries
    for x in entries:
        if x.title == new_name:
            return True
    return False


def check_pwd(password):
    if password == '':
        password = random_pwd(12, 3)
        return password
    else:
        return password


def create_json(item):
    pwds = []
    for x in item.entries:
        var = {"title": f"{x.title}", "user": x.username, "password": x.password, "url": x.url}
        x = [var, json.dumps(var)]
        pwds.append(x)
    return pwds
