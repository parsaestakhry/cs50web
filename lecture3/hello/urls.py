from django.urls import path
# . means the currentf directory
from . import views

urlpatterns = [
    path("", views.index , name="index" ) , 
    path("hello" , views.hello , name="hello"),
    path("batman" , views.batman, name="batman"),
    #any path string is a url pattern
    path("<str:name>" , views.greet , name="greet")
    
    ]   