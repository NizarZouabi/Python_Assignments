from django.shortcuts import render
from time import gmtime, strftime
#from datetime import datetime

# Create your views here.
def index(request):
    time = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'index.html', time)


# time = { "time": datetime.now() } render(request, 'index.html', time)