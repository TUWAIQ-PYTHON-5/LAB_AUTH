from django.urls import path
from . import views

app_name = "Clincs"

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("booking", views.booking, name="booking"),


]


