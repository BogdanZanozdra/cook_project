
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout

# def login(request):
#     return HttpResponse("Login")


def logout_view(request):
    logout(request)
    return redirect('/')



