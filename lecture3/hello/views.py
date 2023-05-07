from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
 
# each view is something that the user might wanna see

def index(request):
    return render(request , "hello/index.html")

def hello(request):
    return HttpResponse("Hello, Parsa!")

def batman(request):
    return HttpResponse("something in the way mmmmm")
# httpresponses can be any html content 
def greet(request , name):
    return render(request, "hello./greet.html", {
        "name" : name.capitalize()
    })