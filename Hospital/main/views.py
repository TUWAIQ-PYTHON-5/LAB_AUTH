from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic,Appointment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def main_page(request : HttpRequest):
    
    return render(request, 'main/index.html')

def clinic_page(request : HttpRequest):
    
    view_clinic = Clinic.objects.all()

    context = {"view_clinics" : view_clinic}
    return render(request, "main/clinic.html", context)

def appointment_page(request : HttpRequest):
    view_clinic = Clinic.objects.all()

    context = {"view_clinics" : view_clinic}
    return render(request, "main/appointment.html", context)

    
def add_clinic(request : HttpRequest):

    if not request.user.has_perm("main.add_clinic"):
        return redirect("main/no_permission.html")

    if request.method == "POST":
        #to add a new entry
        new_clinic = Clinic(name= request.POST["name"], feature_image = request.FILES["feature_image"], description = request.POST["description"], department=request.POST["department"], established_at=request.POST["established_at"])
        new_clinic.save()
        return redirect("main:manage_clinic")


    return render(request, "main/add_clinic.html")

def delete_clinic(request : HttpRequest, clinic_id):

    if not request.user.has_perm("main.delete_clinic"):
       return render(request, "main/no_permission.html")

    clinic = Clinic.objects.get(id=clinic_id)
    clinic.delete()
    return redirect("main:manage_clinic")


def update_clinic(request : HttpRequest, clinic_id):

    if not request.user.has_perm("main.update_clinic"):
        return redirect("main/no_permission.html")

    clinic = Clinic.objects.get(id=clinic_id)
    clinic.established_at = clinic.established_at.isoformat() #to make it compatible with input value in html
    if request.method == "POST":
        clinic.name = request.POST["name"]
        #to check if user chosen a file to upload for the update
        if "feature_image" in request.FILES:
            clinic.feature_image = request.FILES["feature_image"]
        clinic.description = request.POST["description"]
        clinic.department = request.POST["department"]
        clinic.established_at = request.POST["established_at"]

        clinic.save()
        return redirect("main:manage_clinic")

    return render(request, "main/update_clinic.html", {"clinic" : clinic})


def clinic_detail(request : HttpRequest, clinic_id): 

    clinic = Clinic.objects.get(id=clinic_id)
    appointments =  Appointment.objects.filter(clinic=clinic_id)

    return render(request, "main/clinic_detail.html", {"clinic" : clinic, "appointments" : appointments })


def delete_appointment(request : HttpRequest, appointment_id):

    if not request.user.has_perm("main.delete_appointment"):
       return render(request, "main/no_permission.html")
    

    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()
    return redirect("main:manage_appointment")


def add_appointment(request : HttpRequest, clinic_id):

    clinic = Clinic.objects.get(id=clinic_id)
    user : User = request.user
    if request.method == "POST":
        new_appointment = Appointment(clinic=clinic, 
        user=user,
        case_description = request.POST["case_description"], 
        patient_age = request.POST["patient_age"], 
        appointment_datetime = request.POST["appointment_datetime"])
        new_appointment.save()

    return redirect("main:clinic_detail", clinic_id=clinic_id)


def update_appointment(request : HttpRequest, appointment_id):

    if not request.user.has_perm("main.update_appointment"):
       return render(request, "main/no_permission.html")

    appointment = Appointment.objects.get(id=appointment_id)
    appointment.appointment_datetime = appointment.appointment_datetime.isoformat()
    if request.method == "POST":
        appointment.case_description = request.POST["case_description"]

        if "appointment_patient_age" in request.FILES:
            appointment.patient_age = request.POST["patient_age"]
        if "appointment_datetime" in request.FILES:
            appointment.appointment_datetime = request.POST["appointment_datetime"]

        appointment.is_attended = request.POST["is_attended"]
        appointment.save()
        return redirect("main:manage_appointment")

    return render(request, "main/update_appointment.html", {"appointment" : appointment})

def search_clinic(request : HttpRequest):
    if request.method == "POST":
        search = request.POST['search']
        search_clinic = Clinic.objects.filter(name__contains=search)

        return render(request, "main/search.html", {'search_clinic':search_clinic}) 
    else:
        return render(request, "main/search.html", {})

def manage_clinic(request : HttpRequest):
    clinic = Clinic.objects.all()

    context = {"clinics" : clinic}
    return render(request, "main/manage_clinic.html", context)

def manage_appointment(request : HttpRequest):
    appointment = Appointment.objects.all()

    context = {"appointments" : appointment}
    return render(request, "main/manage_appointment.html", context)