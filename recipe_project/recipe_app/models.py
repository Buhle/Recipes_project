from django.db import migrations
from django.db import models
from datetime import datetime
from django.utils import timezone


class Recipes(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images')
    rating = models.CharField(max_length=50)
    prep_time = models.CharField(max_length=50)
    cooking_time = models.CharField(max_length=50)
    servings = models.IntegerField()
    ingredients = models.TextField()
    cooking_instructions = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
