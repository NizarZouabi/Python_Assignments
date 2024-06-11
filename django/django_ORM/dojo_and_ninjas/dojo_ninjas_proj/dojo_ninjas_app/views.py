from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja

# Create your views here.

def index(request):
    context = {
        "dojos":Dojo.objects.all(),
        "ninjas":Ninja.objects.all()
    }
    return render(request, "index.html", context)

def process_form(request):
    if request.method == 'POST':
        form_type = request.POST.get('form')
        if form_type == "dojo":
            name = request.POST.get('name')
            city = request.POST.get('city')
            state = request.POST.get('state')
            new_dojo = Dojo.objects.create(name=name, city=city, state=state)
        elif form_type == "ninja":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            dojo_id = request.POST.get('dojo')
            dojo = Dojo.objects.get(id=int(dojo_id))
            new_dojo_ninja = Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
            
    return redirect('/')

def remove(request):
    if request.method == 'POST':
        dojo_id = request.POST.get('dojo_id')
        dojo_to_remove = Dojo.objects.get(id=int(dojo_id))
        dojo_to_remove.delete()
    
    return redirect('/')