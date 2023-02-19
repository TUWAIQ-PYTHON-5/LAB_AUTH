from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic , Appointment 


# Create your views here.

def index(request : HttpRequest):
    
    result = Clinic.objects.all()
    
    context = {
        
        "clinics":result
    }
    
    return render(request , "main/index.html" , context)


def details(request : HttpRequest , clinic_id):
    
    result = Clinic.objects.get( id = clinic_id)
    context = {
        
        "clinic" : result
    }
    
    return render(request , "main/details.html" , context )
    
def add(request : HttpRequest ):
    
    if request.method == "POST":
           Clinic(
            name = request.POST["name"] ,
            description = request.POST["description"], 
            image = request.FILES["image"],
            ).save()
    
    
    return render(request , "main/add.html" )


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


def appointments_delete(request : HttpRequest , appointment_id ):
    
    appointments = Appointment.objects.get(id=appointment_id)
    appointments.delete()
    
    return render(request , "main/appointment.html")




def appointments_update(request : HttpRequest , appointment_id ):

    appointment = Appointment.objects.get(id = appointment_id)

    if request.method == "POST":
            appointment.patient_age = request.POST["age"]
            appointment.date = request.POST["date"]
            appointment.description = request.POST["description"]
            appointment.save()
            return redirect("url_main:index_page")
    return render(request , "main/appointments_update.html" ,  {"appointment" : appointment})