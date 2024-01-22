from platform import release
from time import timezone
from django.utils import timezone
from xmlrpc.client import _datetime_type
from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    # returns the string representation of the genre name in the DB visualization in browser
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    # date_created = models.DateTimeField(default=datetime.now())
    date_created = models.DateTimeField(default=timezone.now)
