from django.urls import path
from . import views

app_name = 'patient'
urlpatterns = [
    path('signup',views.Register_patiend , name='signUp'),
    path('signin/',views.sign_in , name='signin'),
    path('signout/',views.log_out_user , name='signout'),
    
]