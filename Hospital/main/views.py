from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic, Appointment


# Create your views here.

def index(request : HttpRequest):
    
    clinics = Clinic.objects.all()
    return render(request, "main/index.html",{"clinics": clinics})


def about(request : HttpRequest):
    return render(request, "main/about.html")


# def manage_clinics(request : HttpRequest):
#     return render(request, "main/manage_clinics.html")

def add_clinic(request : HttpRequest):

    if not request.user.is_staff:
        return redirect("main:index_page")

    if request.method == "POST":
        #to add a new entry
        new_clinic = Clinic(name= request.POST["name"], description = request.POST["description"], department = request.POST["department"], established_at=request.POST["addition_date"], feature_image = request.FILES["feature_image"])
        new_clinic.save()
        # return redirect("games:latest_games_page")
    clinics = Clinic.objects.all()

                                                         #  {"form": department}
    return render(request, "main/manage_clinics.html",{"clinics": clinics},)


def update_clinic(request : HttpRequest, clinic_id):
    if not request.user.is_staff:
        return redirect("main:index_page")

    clinic = Clinic.objects.get(id=clinic_id)
    clinic.established_at = clinic.established_at.isoformat() #to make it compatible with input value in html
    if request.method == "POST":
        clinic.name = request.POST["name"]
        clinic.description = request.POST["description"]
        clinic.department = request.POST["department"]
        clinic.established_at = request.POST["established_at"]
        #to check if user chosen a file to upload for the update
        if "feature_image" in request.FILES:
            clinic.feature_image = request.FILES["feature_image"]

        clinic.save()
        return redirect("main:add_clinics_page")

    return render(request, "main/update_clinic.html", {"clinic" : clinic})


def delete_clinic(request : HttpRequest, clinic_id):
    if not request.user.is_staff:
        return redirect("main:index_page")

    clinic = Clinic.objects.get(id=clinic_id)
    clinic.delete()
    return redirect("main:add_clinics_page")

def clinic_detail(request : HttpRequest, clinic_id):

    clinic = Clinic.objects.get(id=clinic_id)
    appointments = Appointment.objects.filter(clinic=clinic)
    if request.user.is_authenticated :
        appointmentsUser = appointments.filter(user = request.user)
        return render(request, "main/clinic_detail.html", {"clinic" : clinic, "appointments" : appointmentsUser})

                                                    
    return render(request, "main/clinic_detail.html", {"clinic" : clinic, "appointments" : appointments})


def search(request : HttpRequest): 

    # display = int(request.GET.get("display", 10)) how many in every page

    if 'search' in request.GET:
        clinics = Clinic.objects.filter(name__contains=request.GET["search"])
    else:
        clinics = Clinic.objects.all()

    context = {"clinics" : clinics}
    return render(request, "main/search.html", context)



def manage_appointments(request : HttpRequest):
    if not request.user.is_staff:
        return redirect("main:index_page")
    
    clinics = Clinic.objects.all()
        
    return render(request, "main/manage_appointments.html",{"clinics": clinics})



def appointments(request : HttpRequest, clinic_id):
    if not request.user.is_staff:
        return redirect("main:index_page")
    
    clinic = Clinic.objects.get(id=clinic_id)
    appointments = Appointment.objects.filter(clinic=clinic)

    if request.method == "POST":
        new_appointment = Appointment(user = request.user, clinic=clinic, case_description = request.POST["case_description"], patient_age = request.POST["patient_age"], appointment_datetime =request.POST["appointment_datetime"])
        new_appointment.save()

                                                    
    return render(request, "main/appointments.html", {"clinic" : clinic, "appointments" : appointments})

    # if request.method == "POST":
    #     new_appointment = Appointment(user = request.user, clinic=request.POST["clinic"], case_description = request.POST["case_description"], patient_age = request.POST["patient_age"])
    #     new_appointment.save()

    # return render(request, "main/appointments.html",{"clinics": clinics})

def delete_appointment(request : HttpRequest, appointment_id):
    if not request.user.is_staff:
        return redirect("main:index_page")

    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()
    return redirect("main:manage_appointments_page")


def book_appointment(request : HttpRequest, clinic_id):
    # if not request.user.is_authenticated:
    #     return redirect("accounts:login_user")
    
    if request.method == "POST":
        clinic = Clinic.objects.get(id=clinic_id)
        new_appointment = Appointment(user = request.user, clinic=clinic, case_description = request.POST["case_description"], patient_age = request.POST["patient_age"], appointment_datetime =request.POST["appointment_datetime"])
        new_appointment.save()

    return redirect("main:detail_clinic_page", clinic_id)

def update_appointment(request : HttpRequest, appointment_id):
    if not request.user.is_staff:
        return redirect("main:index_page")

    appointment = Appointment.objects.get(id=appointment_id)
    appointment.appointment_datetime = appointment.appointment_datetime.isoformat() #to make it compatible with input value in html

    if request.method == "POST":
        appointment.case_description = request.POST["case_description"]
        appointment.patient_age = request.POST["patient_age"]
        if "appointment_datetime" in request.FILES:
            appointment.appointment_datetime = request.POST["appointment_datetime"]
        appointment.appointment_datetime = request.POST["appointment_datetime"] 

        appointment.is_attended = request.POST["is_attended"]
       
        appointment.save()
        return redirect("main:manage_appointments_page")

    return render(request, "main/update_appointment.html", {"appointment" : appointment})



