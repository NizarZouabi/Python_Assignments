from django.shortcuts import render,redirect

# Create your views here.


def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")


def users(request):
    return render(request, "dashboard.html")
