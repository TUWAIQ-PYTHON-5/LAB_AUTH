from django.contrib import admin
from .models import Clinic , Appointment

class ClinicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','feature_image','department', 'established_at')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("clinic","user","case_description","patient_age","appointment_datetime","is_attended")

admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Appointment, AppointmentAdmin)