from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clinc(models.Model):

    name = models.CharField(max_length=1024)
    description = models.TextField()
    HeartCenter = 'HC'
    NeuroscienceCenter = 'NC'
    ObesityCenter = 'OC'
    EyeCenter = 'EC'
    OrthopedicCenter = 'OcC'
    PediatricCenter='PC'
    not_assigen = 'NL'
    departments = [
        (HeartCenter, 'HeartCenter'),
        (NeuroscienceCenter, 'NeuroscienceCenter'),
        (ObesityCenter, 'ObesityCenter'),
        (EyeCenter, 'EyeCenter'),
        (OrthopedicCenter, 'OrthopedicCenter'),
    ]
    departments = models.CharField(
        max_length=3,
        choices=departments,
        default=not_assigen,
    )
    established_at = models.DateField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

    
    def __str__(self) -> str:
        return f"{self.name} "
    


class Review(models.Model):

    clinc = models.ForeignKey(Clinc, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.name} : {self.clinc.name}"
    



class Doctor(models.Model):

    name = models.CharField(max_length=1024)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self) -> str:
        return f"{self.name} "
    


class Appointment(models.Model):
    Relation_clinic = models.ForeignKey(Clinc, on_delete=models.CASCADE)
    Relation_user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_description = models.TextField()
    patient_age =  models.IntegerField()
    appointment_datetime = models.DateTimeField(auto_now_add=True)
    is_attended = models.BooleanField()