from django.shortcuts import render
import datetime
now = datetime.datetime.now()
# Create your views here.
def index(request):
    return render(request, "newyear/index.html" , {
        "newyear" : now.month == 1 and now.day == 1
    })
