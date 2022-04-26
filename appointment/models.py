from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()