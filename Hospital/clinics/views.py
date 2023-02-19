from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.
def home(request : HttpRequest):
    return render(request,"clinics/home.html")

'''def user(request : HttpRequest):
    return render(request,"clinics/home.html")'''

def dtail(request : HttpRequest):
    return render(request,"clinics/dtail.html")

def manager(request : HttpRequest):
    return render(request,"clinics/manager.html")

def search(request : HttpRequest):
    return render(request,"clinics/search.html")
