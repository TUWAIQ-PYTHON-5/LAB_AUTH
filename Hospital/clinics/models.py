from django.db import models

# Create your models here.
class Clinics(models.Model):
    name = models.TextField()
    feature_image = models.ImageField(upload_to="")
    description = models.TextField()
    department = models.TextField()
    established_at = models.IntegerField()
    def __str__(self)->str:
        return f"{self.name}"

class Appointment(models.Model):
    clinics = models.ForeignKey(Clinics, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField(auto_now_add=True)
    is_attended = models.BooleanField(default=False)
    
