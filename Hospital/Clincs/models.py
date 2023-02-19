from django.db import models
from django.contrib.auth.models import User

# Create your models here.



Clinc_dep = (
    ("Heart Center", "Heart Center"),
    ("Neuroscience Center", "Neuroscience Center"),
    ("Obesity Center", "Obesity Center"),
    ("Eye Center", "Eye Center"),
    ("Orthopedic Center", "Orthopedic Center"),
    ("Pediatric Center", "Pediatric Center"))

class Clinic(models.Model):
    name = models.CharField(max_length=1024)
    feature_image = models.ImageField(upload_to="images/", default="images/default.jpg")
    description = models.TextField()
    department = models.CharField(    
        max_length = 50,
        choices = Clinc_dep,
        default = 'Department')
    established_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} "


class Appointment(models.Model):
    Relation_w_clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    Relation_w_user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_description = models.TextField()
    patient_age =  models.IntegerField()
    appointment_datetime = models.DateTimeField(auto_now_add=True)
    is_attended = models.BooleanField()



    def __str__(self) -> str:
        return f"{self.name} : {self.Clincs.name}"





