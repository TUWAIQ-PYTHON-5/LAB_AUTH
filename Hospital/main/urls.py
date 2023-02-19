from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index_page"),
    path("about/", views.about, name="about_page"),
    path("add_clinics/", views.add_clinic, name="add_clinics_page"),
    path("update/clinic/<clinic_id>/", views.update_clinic, name="update_clinic_page"),
    path("delete/clinic/<clinic_id>/", views.delete_clinic, name="delete_clinic_page"),
    path("details/<clinic_id>/", views.clinic_detail, name="detail_clinic_page"),
    path("search/", views.search, name="search_page"),

    path("appointments/", views.manage_appointments, name="manage_appointments_page"),
    path("manage/appointments/<clinic_id>/", views.appointments, name="appointments_page"),
    path("delete/appointmnet/<appointment_id>/", views.delete_appointment, name="delete_appointment_page"),
    path("book/appointemnt/<clinic_id>/", views.book_appointment, name="book_appointment_page"),
    path("update/appointemnt/<appointment_id>/", views.update_appointment, name="update_oppointment_page"),





]