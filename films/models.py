from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title