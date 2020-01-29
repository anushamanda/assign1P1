from django.db import models
from datetime import datetime
from tripadvisors.models import Tripadvisor


class Place(models.Model):
    tripadvisor = models.ForeignKey(Tripadvisor, on_delete=models.CASCADE, related_name='places')
    title = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    ideal_season  = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    minimum_days = models.IntegerField()
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    is_published = models. BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
