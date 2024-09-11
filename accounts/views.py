from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def authenticate_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate_user(request, username=username, password=password)
    if user is not None:
        login(request, user)
        