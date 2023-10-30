from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request,"index.html")

def form(request):
    name = request.POST['name']
    options01 = request.POST['options01']
    options02 = request.POST['options02']
    comment = request.POST['comment']
    data = {
        "name":name,
        "options01":options01,
        "options02":options02,
        "comment":comment
    }
    return render(request, "success.html",data)