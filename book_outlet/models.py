from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=200)
    is_bestselling = models.BooleanField(default=False)
    slug= models.SlugField(default="", null=False, db_index=True, blank=True)
    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"Title: {self.title} | Rating: {self.rating} | Author: {self.author} | Bestselling: {self.is_bestselling}"