from django.db import models
from django.contrib.auth.models import User

DEPARTMENT_CHOICES = (
    ('heart_center', 'Heart Center'),
    ('neuroscience_center', 'Neuroscience Center'),
    ('Obesity_center', 'Obesity Center'),
    ('Eye_center', 'Eye Center'), 
    ('Orthopedic_center','Orthopedic Center'),
    ('Pediatric_center','Pediatric Center'),
)

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    feature_image = models.ImageField(upload_to='clinic_images')
    description = models.TextField()
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    established_at = models.DateField()
   

class Appointment(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_description = models.TextField()
    patient_age = models.PositiveIntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField(default=False)
