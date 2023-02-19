from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Clinic

def home_page(request:HttpRequest):
    return render(request, 'main/home_page.html')

def doctors_page(request:HttpRequest):
    return render(request, 'main/doctors_page.html')

def clinics_page(request:HttpRequest):
    clinic_all = Clinic.objects.all
    clinics_info = {'clinic_all':clinic_all}
    return render(request, 'main/clinics_page.html',clinics_info)



def clinic_details(request:HttpRequest,clinic_id):
    clinic_info = Clinic.objects.get(id=clinic_id)
    return render(request, 'main/clinic_detail_page.html', {'clinic_info':clinic_info})

