from django.db import models

class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=40)


# Create your models here.
