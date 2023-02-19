from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clinic (models.Model):

    name                = models.CharField(max_length=200)
    feature_image       = models.ImageField(upload_to="images/", default="images/default.jpg")
    description         = models.TextField()
    department_choises         = models.TextChoices("department", ['HEART_CENTER', 'NEUROSCIENCE_CENTER', 'OBESITY_CENTER', 'EYE_CENTER', 'ORTHOPEDIC_CENTER', 'PEDIATRIC_CENTER'])
    department = models.CharField(max_length=200, choices= department_choises.choices)
    established_at      = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.name} "


class Appointment (models.Model):

    clinic              = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    case_description    = models.TextField()
    patient_age         = models.CharField(max_length=200)
    appointment_datetime= models.DateField()
    is_attended         = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f"{self.user.first_name} : {self.clinic.n} "

