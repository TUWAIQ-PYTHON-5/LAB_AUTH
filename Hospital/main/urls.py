from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_page, name="Home_page"),
    path('addclinec/', views.addClinec , name='addclinec'),
    path('showall/',views.show_all_clinec,name='allcl'),
    path('update/<clinec_id>' ,views.upadateclinec,name='update'),
    path('delete/<clinec_id>' , views.deletclinec , name='delete'),
    path('addapontment/<clinec_id>' , views.bookForClinec, name='booking'),
    path('showbook/' , views.showUserbook , name="showbook"),
    path('allapointment/<clinec_id>',views.veiw_appointmentin_clinec,name='all_appointment'),
    path('CMapoontmentForClinec/<appointment_id>',views.control_one_appontment_for_clinec,name='cmappontment'),
    path('deleteAppointmentByAdmin/<appointment_id>' , views.delete_userappointment_by_admin,name='deleteappointmentByAdmin'),
    path('addappontmentbyAdmin/' , views.add_appointments_by_admin , name = 'addapontmentbyadmin'),
    path('updateappointmentbyadmin/<appointment_id>' , views.update_appointment_by_admin , name='updateappointmentByAdmin')


    # path("", views.Home_page, name="Home_page"),
    # path("clinics",views.clinics_page, name="clinics_page"),
    # path("register",views.register_page, name="register_page"),
    # path("login",views.login_page, name="login_page"),
    # path("Clinic/add_new",views.add_new_page, name="add_new_page"),
    # path("Booking/Appointment/<clinic_id>" , views.booking , name= "appointment_page"),
    # path("Clinic/details/<clinic_id>/" , views.details_page , name= "clinic_page"),
    # path("Clinic/search/", views.search, name="search"),
    # path("Clinic/appointments/", views.appointments, name="appointments"),
    # path("Clinic/update/<clinic_id>", views.update, name="update"),
    # path("Clinic/delete/<clinic_id>", views.delete, name="delete"),
    # path("logout/", views.logout_user, name="logout_user"),


]
    
    