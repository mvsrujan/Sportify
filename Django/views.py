from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        print(name,password)
        if (name=='Pranav'and password == '123pra456'):
            return render(request,'player.html',{'al':[name]})
        else:
            return render(request,'home.html')
    return render(request,'index.html')
    
def home(request):
    return render(request,'player.html')

def player(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        print(name,password)
        if (name=='Pranav'and password == '123pra456'):
            return render(request,'player.html',{'al':[name]})
        else:
            return render(request,'home.html')
    return render(request,'index.html')
def team(request):
    return render(request,'team.html')