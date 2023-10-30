from django.shortcuts import render

# Create your views here.


def survey(request):
    return render(request, "survey.html")


def new(request):
    return render(request, "new.html")