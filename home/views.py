from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    list=[{'name':'Shalu', 'age':26},
    {'name':'Riyansh', 'age':13},
    {'name':'Anubhavi', 'age':14},
    {'name':'Gaurav', 'age':14},
    {'name':'Neeshu', 'age':29}]

    return render(request, "index.html" , context={'data':list})
   


def hello(request):
    return HttpResponse("<h1> Hello Django</h1>")