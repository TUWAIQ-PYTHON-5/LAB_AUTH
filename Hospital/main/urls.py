from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.Home_page, name="Home_page"),
    path("clinics",views.clinics_page, name="clinics_page"),
    path("register",views.register_page, name="register_page"),
    path("login",views.login_page, name="login_page"),
    path("Clinic/add_new",views.add_new_page, name="add_new_page"),
    path("Booking/Appointment/<clinic_id>" , views.booking , name= "appointment_page"),
    path("Clinic/details/<clinic_id>/" , views.details_page , name= "clinic_page"),
    path("Clinic/search/", views.search, name="search"),
    path("Clinic/appointments/", views.appointments, name="appointments"),
    path("Clinic/update/<clinic_id>", views.update, name="update"),
    path("Clinic/delete/<clinic_id>", views.delete, name="delete"),
    path("logout/", views.logout_user, name="logout_user"),


]
    
    