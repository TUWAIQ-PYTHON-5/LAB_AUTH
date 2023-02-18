from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Clinic, Appointment
from datetime import date


#################################################################
def indexfunction(request : HttpRequest):
    clinics = Clinic.objects.all()
    context = {"clinics" : clinics}
    return render(request, "main/index.html", context)
#################################################################
def userRegisterFun(request : HttpRequest): 
   if request.method == "POST": 
        newUser = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"]) 
        newUser.save() 
        return redirect("main:login")
   return render(request, "main/register.html")
#################################################################
def userAuthFun(request : HttpRequest): 
    msg = None
    if request.method == "POST": 
            user = authenticate(request, username=request.POST["username"], password=request.POST["password"] ) 
            if user is not None:
                login(request, user)
                return redirect(request, "main/index.html")
            else:
                msg = "Try again"
    return render (request,"main/login.html", {"msg":msg} )        
#################################################################
def userLogoutFun(request : HttpRequest):
    logout(request)
    return redirect(request, "main/index.html")
#################################################################
def newClinicFun(request :HttpRequest): 
    if not request.user.is_staff: 
        return redirect("main:login") 
    if request.method == "POST": 
        newClinic = Clinic(name= request.POST["name"], feature_image = request.FILES["feature_image"], description = request.POST["description"], department=request.POST["department"], established_at=request.POST["established_at"]) 
        newClinic.save() 
        return redirect("main:index") 
    return render(request, "main/newClinic.html")
#################################################################
def clinicDetailsFun(request : HttpRequest, clinic_id): 
    clinic = Clinic.objects.get(id=clinic_id) 
    return render(request, "main/clinicDetails.html", {"clinic" : clinic}) 
#################################################################
def updateClinicFun(request : HttpRequest, clinic_id): 
    clinic = Clinic.objects.get(id=clinic_id) 
    clinic.established_at = clinic.established_at.isoformat() 
    if request.method == "POST": 
        clinic.name = request.POST["name"] 
        if "feature_image" in request.FILES: 
            clinic.feature_image= request.FILES["feature_image"] 
        clinic.description      = request.POST["description"] 
        clinic.department       = request.POST["department"] 
        clinic.established_at   = request.POST["established_at"] 
        clinic.save() 
        return redirect("main:index") 
    return render(request, "main/updateClinic.html", {"clinic" : clinic})
#################################################################
def newAppointmentFun(request : HttpRequest, clinic_id): 
    clinic = Clinic.objects.get(id=clinic_id) 
    if request.method == "POST": 
        newAppointment      = Appointment(clinic=clinic,  
        case_description    = request.POST["case_description"],  
        patient_age         = request.POST["patient_age"],  
        appointment_datetime= request.POST["is_attended"],  
        is_attended         = request.POST["case_description"] ) 
        newAppointment.save() 
    return redirect("main/clinicDetails.html", clinic_id=clinic_id) 
#################################################################  
def updateAppointmentFun(request : HttpRequest, appointment_id): 
    appointment = Appointment.objects.get(id=appointment_id) 
    appointment.appointment_datetime = appointment.appointment_datetime.isoformat() 
    if request.method == "POST": 
        appointment.case_description= request.POST["case_description"] 
        appointment.patient_age     = request.POST["patient_age"] 
        if "appointment_datetime" in request.FILES: 
            appointment.appointment_datetime = request.POST["appointment_datetime"] 
        appointment.is_attended = request.POST["is_attended"] 
        appointment.save() 
        return redirect("main:index")
    return render(request, "main/updateAppointment.html", {"appointment" : appointment})
#################################################################
def deleteAppointmentFun(request : HttpRequest, appointment_id): 
    if not request.user.has_perm("main.deleteAppointment"): 
        return render(request, "main/noAccess.html") 
    appointment = Appointment.objects.get(id=appointment_id) 
    appointment.delete() 
    return redirect("main:index") 
#################################################################
def findClinicFun(request : HttpRequest):
    if request.method == "POST":
        toFind = request.POST['toFind']  
        result = Clinic.objects.filter(name__contains=request.POST['toFind'] )
        return render(request, "main/findClinic.html", {'toFind' : toFind , 'result' : result})
    else:
        return render(request, "main/findClinic.html", {'toFind' : toFind})
#################################################################