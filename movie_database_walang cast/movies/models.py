# movies/models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()

    def __str__(self):
        return self.title
