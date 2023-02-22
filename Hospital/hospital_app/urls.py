from django.urls import path
from . import views


app_name = "url_main"

urlpatterns = [
    
    path("" , views.index , name= "index_page"),
    path("Clinic/details/<clinic_id>/" , views.details , name= "clinic_page"),
    path("Clinic/new/add" , views.add , name= "add_clinic"),
    path("Booking/Appointment/<clinic_id>" , views.booking , name= "appointment_page"),
    path("Clinic/search/", views.search, name="search"),
    path("Clinic/mange/", views.mange, name="mange_clinic"),
    path("Clinic/appointments/", views.appointments, name="appointments"),
    path("Clinic/update/<clinic_id>", views.update, name="update"),
    path("Clinic/delete/<clinic_id>", views.delete, name="delete"),
    path("Appointment/delete/<appointment_id>", views.appointments_delete, name="appointments_delete"),
    path("Appointment/update/<appointment_id>", views.appointments_update, name="appointments_update"),
   user.has_perm('conenttypes')
    # path("Contact/" , views.contact , name= "contact_page"),
]