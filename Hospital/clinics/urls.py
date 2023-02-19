from django.urls import path
from . import views

name_app = "clinics"

urlpatterns=[
    path('',views.home,name="home_page")
]