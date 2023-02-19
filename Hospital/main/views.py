from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic, Appointment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout




# Create your views here.

def Home_page(request : HttpRequest):
    result = Clinic.objects.all()
    
    context = {
        
        "clinics":result
    }
    
    return render(request, "main/Home.html",context)


def details_page(request : HttpRequest , clinic_id):
    result = Clinic.objects.get( id = clinic_id)
    context = {
        
        "clinic" : result
    }
    return render(request, "main/details.html",context)



def add_new_page(request : HttpRequest):
    if request.method == "POST":
           Clinic(
            name = request.POST["name"] ,
            description = request.POST["description"], 
            image =request.FILES["image"]
            ).save()
    
    return render(request, "main/add_new.html")


def booking(request : HttpRequest , clinic_id):
    msg = "Appointment date booked"
    if request.method == "POST":
            
        clinic = Clinic.objects.get(id = clinic_id)
        check_date= Appointment.objects.filter(date__gt= request.POST["date"])
        if check_date:
            return render(request ,"main/booking.html" ,{"msg" :msg})
        else:
            Appointment(
            clinic= clinic,
            user = request.user,
            date = request.POST["date"],
            patient_age = request.POST["age"],
            description = request.POST["description"]).save()
            
        return redirect("url_main:appointment_page" , clinic_id = clinic_id )
    return render(request, "main/booking.html")



def search(request : HttpRequest):

    if request.method == "GET": 

            name =  request.GET.get('search')      
            search = Clinic.objects.filter(name__contains = name)
               
            return render(request , "main/search.html" , {"search" : search})



def delete(request : HttpRequest, clinic_id):
    post = Clinic.objects.get(id=clinic_id)
    post.delete()
    return redirect("url_main:index_page")



def update(request : HttpRequest , clinic_id ):

    clinic = Clinic.objects.get(id = clinic_id)

    if request.method == "POST":
            clinic.name = request.POST["name"]
            clinic.description = request.POST["description"]
            clinic.image = request.FILES["image"]
            clinic.save()
            return redirect("url_main:index_page")
    return render(request , "main/update.html" ,  {"clinic" : clinic})



def mange(request : HttpRequest):
    
    result = Clinic.objects.all()
    context = {
        
        "clinics":result
    }
    
    return render(request , "main/mange.html" , context)

    

def appointments (request : HttpRequest ):
    
    result = Appointment.objects.all()
    
    context = {
        
        "appointments":result
    }
    
    return render(request , "main/appointment.html" , context)
    



def login_page(request : HttpRequest):
     loggin_msg = None
    
     if request.method == "POST":
        #authenticate user credentials
        user = authenticate(request, username= request.POST["username"], password = request.POST["password"] )

        if user is not None:
            #login user
            login(request, user)
            return redirect("url_main:index_page")
        else:
            loggin_msg = "Please Use correct Credentials"

     return render(request, "accounts/login.html", {"msg" : loggin_msg})
     return render(request, "main/login.html")

def logout_user(request : HttpRequest):

    logout(request)

    return redirect("url_main:base_page")

def clinics_page(request : HttpRequest):
    return render(request, "main/clinics.html")



def register_page(request : HttpRequest):
    if request.method == "POST":
        new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
        new_user.save()
    return redirect("main:login_user")
    
    return render(request, "main/register.html")
        
    

 



