from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
path("home/", views.home_page, name="home_page"),
path("add_clinic",views.add_clinic,name="add_clinic"),
path("detail/<clinic_id>/", views.detail_page, name="detail_page"),
path("",views.base_page,name="base_page"),
path("update/<clinic_id>/", views.update_clinic, name="update_clinic"),
path("delete/<clinic_id>/", views.delete_clinic, name="delete_clinic"),
path("search/",views.search_page,name='search_page'),
path("add_appointment/",views.add_appointment,name="add_appointment"),
path("show_appointment/",views.show_appointment,name="show_appointment"),
path("appointment_detail/<appointment_id>/", views.appointment_detail, name="appointment_detail"),
path("appointment_update/<appointment_id>/", views.update_appointment, name="update_appointment"),
path("delete_appointment/<appointment_id>/", views.delete_appointment, name="delete_appointment"),
path("book_appointment/",views.book_appointment,name="book_appointment"),
path("prev_appoint/",views.prev_appoint,name="prev_appoint"),



]
