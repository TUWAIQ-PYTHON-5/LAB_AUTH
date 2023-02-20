from django.db import models
from django.contrib.auth.models import User



class Clinic(models.Model):
     DEPARTMENT_CHOICES=(('Heart Center','Heart Center'),('Neuroscience Center','Neuroscience Center'),('Obesity Center', 'Obesity Center'),('Eye Center', 'Eye Center'),('Orthopedic Center','Orthopedic Center'),('Pediatric Center','Pediatric Center'),)

     name=models.CharField(max_length=1024)
     feature_image= models.ImageField(upload_to="images/", default="images/default.jpg")
     description=models.TextField()
     department=models.CharField(max_length=300,choices=DEPARTMENT_CHOICES)
     established_at=models.DateTimeField()



class Appointment(models.Model):
     TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)
     clinic=models.ForeignKey(Clinic,on_delete=models.CASCADE)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     case_description= models.TextField()
     patient_age=models.IntegerField()
     appointment_datetime=models.DateTimeField()
     is_attended=models.BooleanField(default=False)
    

