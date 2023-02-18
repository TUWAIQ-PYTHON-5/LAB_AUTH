from django.db import models
from django.contrib.auth.models import User


# Create your models here.
department_choices = (
        ("Heart Center", "Heart Center"),
        ("Neuroscience Center", "Neuroscience Center"),
        ("Obesity Center", "Obesity Center"),
        ("Eye Center", "Eye Center"),
        ("Orthopedic Center", "Orthopedic Center"),
        ("Pediatric Center", "Pediatric Center"), )


class Clinic(models.Model):

    name = models.CharField(max_length=700)
    feature_image = models.ImageField(upload_to="images/")
    description = models.TextField()
    department =models.CharField(max_length=1000,choices=department_choices)
    established_at = models.DateTimeField(auto_now_add=True)


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_description = models.TextField()
    patient_age=models.IntegerField()
    appointment_datetime=models.DateTimeField(auto_now_add=True)
    is_attended=models.BooleanField()



