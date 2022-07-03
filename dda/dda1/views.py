import json

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.template.response import TemplateResponse
from .forms import NameForm, RegForm

import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Create your views here.

config = {
    "apiKey": "AIzaSyAPppt439TK0Xra0JrUXzPG5Y_nzwjw9VM",
    "authDomain": "ven-u-book.firebaseapp.com",
    "projectId": "ven-u-book",
    "storageBucket": "ven-u-book.appspot.com",
    "messagingSenderId": "723635461555",
    "appId": "1:723635461555:web:e02e9de3466872a4867fc6",
    "measurementId": "G-JC4YK9DC8J",
    "databaseURL": "https://ven-u-book-default-rtdb.firebaseio.com/"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
flag = None


def reads(request, checkuser1):
    request.session['_old_post'] = request.POST
    print(request.session.get('_old_post'))
    if request.method != 'POST':
        return HttpResponse("invalid attempt")
    return redirect("sup", check=checkuser1)


def say_hello(request):
    form = NameForm()
    if request.method == 'POST':
        return get_name(request)
    elif request.method == 'GET':

        return render(request, 'index.html', {'form': form})
    else:

        return render(request, 'index.html', {'form': form})


def superad(request, check):
    print(request)
    old_post = request.session.get('_old_post')
    print(old_post)
    if old_post == 'POST':
        return render(request, 'admin.html', {"name": check})
    else:
        return HttpResponse("invalid attempt")


def reg(request):
    if request.method == 'POST':
        return insert(request)

    form = RegForm()
    return render(request, 'reg.html', {'form': form})


def get_name(request):
    x = database.child('count').get().val()
    list1 = []
    global flag
    checkuser1 = ""
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            n = form.cleaned_data["name"]
            np = form.cleaned_data["pasn"]
            data = {

                "name": n,
                "pass": np,
            }

            # database.child('user').child(x).set(data)
            # database.child('count').set(x + 1)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            person = database.child('user').shallow().get().val()
            for i in person:
                list1.append(i)
            list1.sort()
            print(list1)
            for i in list1:
                checkuser1 = database.child("user").child(i).child("name").get().val()
                checkpass = database.child("user").child(i).child("pass1").get().val()
                print(checkuser1, checkpass)
                if checkuser1 == n and checkpass == np:
                    flag = "accept"
                    break

    # if a GET (or any other method) we'll create a blank form
    if flag == "accept":
        print("inside1")
        flag = ""
        return reads(request, checkuser1)
    else:
        print("inside 2")
        form = NameForm()
        flag = "reject"
        return render(request, 'index.html', {'flag': flag, 'form': form})


def insert(request):
    x = database.child('count').get().val()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            n = form.cleaned_data["name"]
            np1 = form.cleaned_data["pasn1"]
            np2 = form.cleaned_data["pasn2"]
            npe = form.cleaned_data["email"]
            print(np1, np2)
            data = {

                "name": n,
                "pass1": np1,

                "email": npe, }
            if np1 == np2:
                print(np1, np2)
                database.child('user').child(x).set(data)
                database.child('count').set(x + 1)
                recpientlist = [npe, ]
                send_mail("Welcome to VEN U BOOK", "THANK YOU FOR REGISTERING", "allenanand2001@gmail.com",
                          recpientlist, auth_password="Allenisgreat1")
                return HttpResponseRedirect("/home/")
            else:
                er1 = "Password doesnt match"

                print(er1)
                form = RegForm()
                return render(request, 'reg.html', {'error': er1, 'form': form})
