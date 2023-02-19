from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Clinic(models.Model):

    CLINIC_CHOICES = (
        ("HEART_CENTER","Heart Center"), 
        ("NEUROSCIENCE_CENTER","Neuroscience Center"), 
        ("OBESITY_CENTER","Obesity Center"), 
        ("EYE_CENTER","Eye Center"),
        ("ORTHOPEDIC_CENTER","Orthopedic Center"),
        ("PEDIATRIC_CENTER","Pediatric Center"),
    )
    name = models.CharField(max_length=1024)
    feature_image = models.ImageField(upload_to="images/", default="images/default.jpg")
    description = models.TextField()
    department = models.CharField(max_length=19,choices=CLINIC_CHOICES,default="EYE_CENTER")
    established_at = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.name} "

class Appointment(models.Model):

    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateField()
    is_attended = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user.first_name} : {self.clinic.name}"

