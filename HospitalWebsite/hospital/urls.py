from django.urls import path
from . import views

app_name = "hospital"

urlpatterns = [
    path("", views.home, name="home page"),
    path("detail/<clinic_id>/", views.details, name="details_page"),
    path("add/clinic/", views.add_clinic, name="add_clinic"),
    path("update/clinic/<clinic_id>/", views.update_clinic, name="update_clinic"),
    path("delete/clinic/<clinic_id>/", views.delete_clinic, name="delete_clinic"),
    path("appointments", views.appointments, name="appointments"),
    path("search/", views.search, name="search" ),
    path("add/appointment/", views.add_appointment, name="add_appointment"),
    path("update/appointment/<appointment_id>/", views.update_appointment, name="update_appointment"),
    path("delete/appointment/<appointment_id>/", views.delete_appointment, name="delete_appointment"),
    path("detail_2/<appointment_id>/", views.details_2, name="details_page_2"),

]
