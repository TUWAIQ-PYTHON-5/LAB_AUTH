from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("search/", views.search_clinic, name="search"),

    path("add/<clinic_id>", views.add_appointment, name="add_appointment"),
    path("update/appointment/<appointment_id>/", views.update_appointment, name="update_appointment"),
    path("delete/appointment/<appointment_id>/", views.delete_appointment, name="delete_appointment"),
    path("appointment/", views.appointment_page, name="appointment_page"),
    path("manage/appointment", views.manage_appointment, name="manage_appointment"),
    
    path("details/<clinic_id>/", views.clinic_detail, name="clinic_detail"),
    path("add_clinic/", views.add_clinic, name="add_clinic"),
    path("update/clinic/<clinic_id>/", views.update_clinic, name="update_clinic"),
    path("delete/clinic/<clinic_id>/", views.delete_clinic, name="delete_clinic"),
    path("clinic/", views.clinic_page, name="clinic_page"),
    path("manage/clinic/", views.manage_clinic, name="manage_clinic"),
]