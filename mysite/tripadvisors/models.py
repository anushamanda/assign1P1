from django.db import models
from datetime import datetime


class Tripadvisor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    phone = models.IntegerField()
    mail_id = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
