from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index_page"),
    path("about/", views.about, name="about_page"),
    path("add_clinics/", views.add_clinic, name="add_clinics_page"),
    path("update/<clinic_id>/", views.update_clinic, name="update_clinic_page"),
    path("delete/<clinic_id>/", views.delete_clinic, name="delete_clinic_page"),
    path("details/<clinic_id>/", views.clinic_detail, name="clinic_detail_page"),
    path("search/", views.search, name="search_page"),

    path("manage_appointemnts/", views.manage_appointments, name="manage_appointments_page"),
    path("book_appointemnt/", views.book_appointment, name="book_appointment_page"),



]