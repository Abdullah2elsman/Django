from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField()
    published_date = models.DateField()
