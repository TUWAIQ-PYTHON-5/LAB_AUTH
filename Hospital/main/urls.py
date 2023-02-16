from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("add/<clinic_id>/", views.add_appointment, name="add_appointment"),
    path("update/<appointment_id>/", views.update_appointment, name="update_appointment"),
    path("delete/<appointment_id>/", views.delete_appointment, name="delete_appointment"),
    path("details/<clinic_id>/", views.clinic_detail, name="clinic_detail"),
    path("add/", views.add_clinic, name="add_clinic"),
    path("update/<clinic_id>/", views.update_clinic, name="update_clinic"),
    
]