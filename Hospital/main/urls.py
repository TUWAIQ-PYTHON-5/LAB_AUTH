from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("",                         views.indexfunction,        name="index"),
    path("register",                 views.userRegisterFun,      name="register"),
    path("login",                    views.userAuthFun,          name="login"),
    path("add/",                     views.newClinicFun,         name="newClinic"),
    path("details/<clinic_id>/",     views.clinicDetailsFun,     name="clinicDetails"),
    path("update/<clinic_id>/",      views.updateClinicFun,      name="updateClinic"),
    path("find/",                    views.findClinicFun,        name="findClinic" ),
    path("addA/<clinic_id>/",        views.newAppointmentFun,    name="addAppointment"),
    path("updateA/<appointment_id>/",views.updateAppointmentFun, name="updateAppointment"),
    path("deleteA/<appointment_id>/",views.deleteAppointmentFun, name="deleteAppointment"),
    
    
]##