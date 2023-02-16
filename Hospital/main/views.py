from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic,Appointment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def main_page(request : HttpRequest):
    
    return render(request, 'main/index.html')


def register_user(request : HttpRequest):

    if request.method == "POST":
        new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
        new_user.save()

        #if register successful redirect to sign in page
        return redirect("accounts:login_user")


    return render(request, "accounts/register.html")


def login_user(request : HttpRequest):

    loggin_msg = None
    
    if request.method == "POST":
        #authenticate user credentials
        user = authenticate(request, username= request.POST["username"], password = request.POST["password"] )

        if user is not None:
            #login user
            login(request, user)
            return redirect("main:index_page")
        else:
            loggin_msg = "Please Use correct Credentials"

    return render(request, "accounts/login.html", {"msg" : loggin_msg})



def logout_user(request : HttpRequest):

    logout(request)

    return redirect("main:main_page")

    
def add_clinic(request : HttpRequest):

    if not request.user.is_staff:
        return redirect("accounts:login_user")

    if request.method == "POST":
        #to add a new entry
        new_clinic = Clinic(name= request.POST["name"], feature_image = request.FILES["feature_image"], description = request.POST["description"], department=request.POST["department"], established_at=request.POST["established_at"])
        new_clinic.save()
        return redirect("main:mian_page")


    return render(request, "main/add_clinic.html")


def update_clinic(request : HttpRequest, clinic_id):

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
        return redirect("main:main_page")

    return render(request, "main/update_clinic.html", {"clinic" : clinic})


def clinic_detail(request : HttpRequest, clinic_id):

    clinic = Clinic.objects.get(id=clinic_id)

    return render(request, "clinic/clinic_detail.html", {"clinic" : clinic})


def delete_appointment(request : HttpRequest, appointment_id):

    if not request.user.has_perm("main.delete_appointment"):
       return render(request, "main/no_permission.html")
    

    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()
    return redirect("main:main_page")


def add_appointment(request : HttpRequest, clinic_id):

    clinic = Clinic.objects.get(id=clinic_id)
    if request.method == "POST":
        new_appointment = Appointment(clinic=clinic, 
        case_description = request.POST["case_description"], 
        patient_age = request.POST["patient_age"], 
        appointment_datetime = request.POST["is_attended"], 
        is_attended = request.POST["case_description"] )
        new_appointment.save()

    return redirect("clinic:clinic_detail", clinic_id=clinic_id)


def update_appointment(request : HttpRequest, appointment_id):

    appointment = Appointment.objects.get(id=appointment_id)
    appointment.appointment_datetime = appointment.appointment_datetime.isoformat()
    if request.method == "POST":
        appointment.case_description = request.POST["case_description"]
        appointment.patient_age = request.POST["patient_age"]
        if "appointment_datetime" in request.FILES:
            appointment.appointment_datetime = request.POST["appointment_datetime"]
        appointment.is_attended = request.POST["is_attended"]
        appointment.save()
        return redirect("main:main_page")

    return render(request, "main/update_appointment.html", {"appointment" : appointment})
