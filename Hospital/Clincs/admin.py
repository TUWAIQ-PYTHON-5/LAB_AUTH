from django.contrib import admin
from .models import Clinic, Appointment
# Register your models here.


#to customize the panel
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'department')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('Relation_w_clinic', 'case_description')
    list_filter = ('appointment_datetime',)

admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Appointment, AppointmentAdmin)

