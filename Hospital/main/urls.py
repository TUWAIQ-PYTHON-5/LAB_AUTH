from django.urls import path 
from . import views


app_name = 'main'

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('clinics/',views.clinics_page,name='clinics_page'),
    path('clinic/<clinic_id>/',views.clinic_details,name='clinic_details'),
    path('appointment/',views.appointment_page,name='appointment_page'),
    path('save_appointment/',views.save_appointment,name='save_appointment'),

   
]
