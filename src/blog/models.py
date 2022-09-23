from django.db import models

# Create your models here.

class Movie(models.Model):
    name=models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    rating=models.FloatField(default=0.0)
    image=models.ImageField(upload_to='movies',blank=True, null=True)

