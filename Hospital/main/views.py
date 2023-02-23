from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic , Appointment
from django.contrib.auth.decorators import login_required


def home_page(request:HttpRequest):
    return render(request, 'main/home_page.html')

def clinics_page(request:HttpRequest):
    clinic_all = Clinic.objects.all
    clinics_info = {'clinic_all':clinic_all}
    return render(request, 'main/clinics_page.html',clinics_info)



def clinic_details(request:HttpRequest,clinic_id):
    clinic_info = Clinic.objects.get(id=clinic_id)
    return render(request, 'main/clinic_detail_page.html', {'clinic_info':clinic_info})

@login_required(login_url='/accounts/login/')
def appointment_page(request:HttpRequest):
    clinics = Clinic.objects.all()
    if request.method == 'POST':
        clinic_name = request.POST['clinic_select']
        clinic = Clinic.objects.get(name=clinic_name)
        Appointment(
            clinic=clinic,
            user=request.user,
            case_description=request.POST['case_description'],
            patient_age=request.POST['patient_age'],
            appointment_datetime=request.POST['appointment_datetime'],
        ).save()
        return redirect('main:home_page')
    return render(request, 'main/appointment_page.html', {'clinics':clinics})

def save_appointment(request:HttpRequest):
    pass
        
        

