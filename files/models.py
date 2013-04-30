from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='img/headimg')

class BackCar(models.Model):
    picture = models.ImageField(upload_to='img/headimg')

class LargeFile(models.Model):
    lfile = models.FileField(upload_to='video')