from django.db import models

# Create your models here.


class Player(models.Model):
    token = models.CharField(max_length=256, default='shoikh123', blank=False, null=False)
    name = models.CharField(max_length=256, default='Shaik', blank=False, null=False)
