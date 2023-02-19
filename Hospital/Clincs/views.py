from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Appointment


# Create your views here.

def index(request : HttpRequest):
    return render(request, 'Clincs/index.html')

def home(request : HttpRequest):
    return render(request, 'Clincs/home.html')


def booking(request : HttpRequest):
    if not request.user.is_staff:
        return redirect("accounts:login_user")
    if request.method == "POST":
        #to add a new entry
        booking = Appointment(name= request.POST["name"],
        feature_image = request.FILES["feature_image"])
        description = request.POST["description"], 
        department = request.POST["department"], 
        booking.save()
        return redirect("Clincs:index")
    return render(request, "Clincs/booking.html")
