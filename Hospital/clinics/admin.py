from django.contrib import admin
from .models import Clinics, Appointment
# Register your models here.

class ClinicsAdmin(admin.ModelAdmin):
    list_display = ("name" ,"established_at")

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("case_description" , "appointment_datetime" ,"is_attended")



admin.site.register(Clinics, ClinicsAdmin)
admin.site.register(Appointment, AppointmentAdmin)
