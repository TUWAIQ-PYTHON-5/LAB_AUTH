from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

    path("", views.index_page, name="index_page"),
    path("departments/", views.show_all_clinc, name="departments_page"),
    path("doctors/", views.show_all_doctor, name="doctors_page"),
    path("about/", views.about_page, name="about_page"),
    path("contact/", views.contact_page, name="contact_page"),
    path("add/", views.add_clinc, name="add_new_clinc"),
    path("add_doctor/", views.add_doctor, name="add_new_doctor"),
    path("update/<clinc_id>/", views.update_clinc, name="update_clinc"),
    path("delete/<clinc_id>/", views.delete_clinc, name="delete_clinc"),
    path("details/<clinc_id>/", views.clinc_detail, name="clinc_detail"),
    path("review/add/<clinc_id>/", views.add_review, name="add_review"),
    path("search/", views.search_clinc, name="search_clinc"),


    path("manage_appointemnts/", views.manage_appointments, name="manage_appointments_page"),
    path("book_appointemnt/", views.book_appointment, name="book_appointment_page"),
    


]