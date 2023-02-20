from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic,Appointment
from django.contrib.auth.models import User

def home_page(request:HttpRequest):

    show_clinic = Clinic.objects.all()
    return render(request, "main/home.html", {"show_clinic" :show_clinic})


def add_clinic(request:HttpRequest):
    if request.method == "POST":
        new_clinic= Clinic(name= request.POST["name"], description= request.POST["description"], feature_image= request.FILES["feature_image"],department=request.POST["department"], established_at=request.POST["established_at"])
        new_clinic.save()
        return redirect("main:home_page")

    return render(request,"main/add_clinic.html")

def detail_page(request:HttpRequest,clinic_id):
    clinic=Clinic.objects.get(id=clinic_id)
    return render(request, "main/detail.html",{"clinic":clinic})
def base_page(request:HttpRequest):
    return render(request,"main/base.html")



def search_page(request:HttpRequest):
       if request.method=="POST":
        searched= request.POST['searched'] 
        search_clinic=Clinic.objects.filter(name__contains=searched)

        return render(request, "main/search.html", {'searched':searched,'search_clinic':search_clinic})
       else:
        return render(request, "main/search.html", {})

def update_clinic(request:HttpRequest,clinic_id):
    
    clinic= Clinic.objects.get(id=clinic_id)
    if request.method == "POST":
        clinic.name=request.POST["name"]
        clinic.description = request.POST["description"]
        clinic.department=request.POST["department"] 
        clinic.established_at=request.POST["established_at"]
        if "feature_image" in request.FILES:
            clinic.feature_image = request.FILES["feature_image"]
        
        clinic.save()
        return redirect("main:home_page")
    
    return render(request, "main/update_clinic.html", {"clinic" : clinic})

def delete_clinic(request : HttpRequest, clinic_id):
    if not request.user.has_perm("main.delete_clinic"):
       return render(request, "main/no_permission.html")
    
    clinic=Clinic.objects.get(id=clinic_id)
    clinic.delete()
    return redirect("main:home_page")
    

def add_appointment(request:HttpRequest):
    if request.method == "POST":

        new_appointment= Appointment(user=request.user,clinic_name= Clinic.objects.filter(clinic_name='clinic_name'),case_description = request.POST["case_description"],patient_age=request.POST["patient_age"],appointment_datetime=request.POST["appointment_datetime"])
        new_appointment.save()
        return redirect("main:home_page")

    return render(request,"main/add_appointment.html")
def show_appointment(request:HttpRequest):
    show_appointment =Appointment.objects.all()
    return render(request, "main/show_appointment.html", {"show_appointment" :show_appointment})

                  
def update_appointment(request:HttpRequest,appointment_id):
    
    appointment=Appointment.objects.get(id=appointment_id)

    appointment.user = request.user
    appointment.clinic_name =request.POST["clinic_name"]
    appointment.case_description =request.POST["case_description"]
    appointment.patient_age=request.POST["patient_age"]
    appointment.appointment_datetime=request.POST["appointment_datetime"]

    appointment.save()
    return redirect("main:home_page")
    return render(request, "main/update_appointment.html", {"appointment" : appointment})
def delete_appointment(request : HttpRequest, appointment_id):
    if not request.user.has_perm("main.delete_appointment"):
       return render(request, "main/no_permission.html")
    
    appointment=Appointment.objects.get(id=appointment_id)
    appointment.delete()
    return redirect("main:home_page")
def appointment_detail(request:HttpRequest,appointment_id):
    appointment=Appointment.objects.get(id=appointment_id)
    return render(request,"main/detail_appointment.html",{"appointment":appointment})


def book_appointment(request:HttpRequest):

    if request.method == "POST":
        book_appointment=Appointment(user=request.user,
                                      appointment_datetime=request.POST["appointment_datetime"],
                                      patient_age=request.POST["patient_age"])
        book_appointment.save()
    
        return redirect("main:home_page")

    return render(request,"main/book_appoint.html",)


def prev_appoint(request:HttpRequest):    
    prev_appoint= Appointment.objects.filter(user= request.user)

    return render(request, "main/prev_appoint.html",{"prev_appoint":prev_appoint})