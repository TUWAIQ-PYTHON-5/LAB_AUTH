from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User






class Clinic(models.Model):
    
    name = models.CharField(max_length=1024)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    established_at = models.DateField(default= timezone.now )
    HeartCenter = 'HC'
    NeuroscienceCenter = 'NC'
    ObesityCenter = 'OC'
    OrthopedicCenter = 'ORC'
    PediatricCenter = 'PC'
    Department = (
    (HeartCenter , 'Heart Center'),
    (NeuroscienceCenter , 'Neuroscience Center') ,
    (ObesityCenter , 'Obesity Center') ,
    (OrthopedicCenter , 'Orthopedic Center') ,
    (PediatricCenter , 'Pediatric Center') ,
    )
    department = models.CharField(max_length= 10,choices=Department , default= HeartCenter)
    
    
    
    def __str__(self) -> str:
        return f"{self.name}"

    

class Appointment(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_age = models.IntegerField(default= 20)
    date  = models.DateTimeField( )
    description = models.TextField()
    is_attended  = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f"{self.clinic}"
    
    