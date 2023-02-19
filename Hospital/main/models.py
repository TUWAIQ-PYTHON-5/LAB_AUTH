from django.db import models
from django.contrib.auth.models import User


# Create your models here.

department_CHOICES = (
        ("Heart Center", "Heart Center"),
        ("Neuroscience Center", "Neuroscience Center"),
        ("Obesity Center", "Obesity Center"),
        ("Eye Center", "Eye Center"),
        ("Orthopedic Center", "Orthopedic Center"),
        ("Pediatric Center", "Pediatric Center"),
    )

class Clinic(models.Model):

    name = models.CharField(max_length=1024)
    feature_image = models.ImageField(upload_to="img/", default="img/default.jpg") 
    description = models.TextField()
    department = models.CharField(max_length=50, default= "", choices=department_CHOICES)
    established_at = models.DateField()

    def __str__(self) -> str:
        return f"{self.name} "


class Appointment(models.Model):

    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_description = models.TextField()
    patient_age =  models.IntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name} : {self.clinic.name}"



