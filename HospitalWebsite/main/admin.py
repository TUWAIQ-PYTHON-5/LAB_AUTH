
from django.contrib import admin
from .models import Clinic,Appointment
# Register your models here.


#to customize the panel
class ClinicAdmin(admin.ModelAdmin):
     list_display = ['name','description','feature_image','department','established_at',]
class AppointmentAdmin(admin.ModelAdmin):
     list_display = ('user','clinic','case_description','patient_age','appointment_datetime','is_attended')


admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Appointment, AppointmentAdmin)
