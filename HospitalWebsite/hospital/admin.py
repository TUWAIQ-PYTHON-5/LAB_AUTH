from django.contrib import admin
from .models import Clinic ,Appointment
# Register your models here.



class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'feature_image', 'description','department','established_at')
   

admin.site.register(Clinic,ClinicAdmin)



class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'case_description', 'patient_age','appointment_datetime','is_attended')
   

admin.site.register(Appointment,AppointmentAdmin)
