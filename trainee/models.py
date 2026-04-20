from django.db import models

class Trainee(models.Model):
    name = models.CharField(max_length=100)
    