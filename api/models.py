from django.db import models

# Create your models here.


class Toggle(models.Model):
    value = models.BooleanField(default=False)

class DataLog(models.Model):
    time = models.DateTimeField(auto_now_add=True)

class Config(models.Model):
    delay = models.IntegerField(default=1000)