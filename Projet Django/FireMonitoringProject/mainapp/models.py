from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class FireMonitoringData(models.Model):
    location = models.CharField(max_length=255)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
