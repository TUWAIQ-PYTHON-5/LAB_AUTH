from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic,Appointment

# Create your views here.
def home(request : HttpRequest):
    latest_clinic = Clinic.objects.all()
    context = {"latest_clinic" : latest_clinic}
    return render(request,'hospital/home.html',context)

 



def details(request : HttpRequest,clinic_id):
    clinic=Clinic.objects.get(id=clinic_id)
    return render(request,'hospital/detail.html', {"clinic" : clinic })





def add_clinic(request : HttpRequest):
    
    if not request.user.is_staff:
       return redirect("accounts:login_user")


    if request.method == "POST":
        #to add a new entry
        new_clinic = Clinic(name= request.POST["name"], feature_image = request.FILES["feature_image"], description = request.POST["description"], department=request.POST["department"], established_at = request.POST["established_at"])
        new_clinic.save()
        return redirect("hospital:home page")


    return render(request,'hospital/add_clinic.html')




def update_clinic(request : HttpRequest,clinic_id):
 clinic = Clinic.objects.get(id=clinic_id)
 if request.method == "POST":
        clinic.name = request.POST["name"]
        if "feature_image" in request.FILES:
           clinic.feature_image = request.FILES["feature_image"]
        clinic.description = request.POST["description"]
        clinic.department = request.POST["department"]
        clinic.save()
        return redirect("hospital:home page")
 return render(request,'hospital/update_clinic.html',{"clinic":clinic})




def delete_clinic(request : HttpRequest,clinic_id):
    del_clinic = Clinic.objects.get(id=clinic_id)
    del_clinic.delete()
    return redirect("hospital:home page")



def search(request : HttpRequest):
  if request.method=="POST":
        user_input= request.POST['user_input'] 
        clinic =Clinic.objects.filter(name__contains=user_input)
        return render(request, "hospital/search.html", {'clinic':clinic})
  


  
#### part 2

def appointments(request : HttpRequest):
    latest_appointments = Appointment.objects.all()
    context = {"latest_appointments" : latest_appointments}
    return render(request,'hospital/appointments.html',context)


def details_2(request : HttpRequest,appointment_id):
    appointment=Appointment.objects.get(id=appointment_id)
    return render(request,'hospital/detail_2.html', {"appointment" : appointment })



def add_appointment(request : HttpRequest):

    if request.method == "POST":
        new_appointment= Appointment(user=request.user ,case_description=request.POST["case_description"], patient_age = request.POST["patient_age"],appointment_datetime=request.POST["appointment_datetime"], is_attended = request.POST["is_attended"])
        new_appointment.save()
        return redirect("hospital:home page")

    return render(request,'hospital/add_appointment.html')




def update_appointment(request : HttpRequest,appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == "POST":

            appointment.case_description = request.POST["case_description"]
            appointment.patient_age = request.POST["patient_age"]
            appointment.is_attended = request.POST["appointment_datetime"]
            appointment.description = request.POST["is_attended"]
            appointment.save()
            return redirect("hospital:appointments")
    return render(request,'hospital/update_appointment.html',{"appointment":appointment})




def delete_appointment(request : HttpRequest,appointment_id):
    del_appointment = Appointment.objects.get(id=appointment_id)
    del_appointment.delete()
    return redirect("hospital:appointments")
