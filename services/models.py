from django.db import models
class Service(models.Model):
    service_logo=models.CharField(max_length=90)
    service_des=models.TextField()
    service_img=models.CharField(max_length=50)
    service_head=models.CharField(max_length=50)
    service_rat=models.CharField(max_length=50)

# Create your models here.
