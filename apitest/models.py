from csv import writer
from django.db import models

# Create your models here.


class Singer(models.Model):
    title = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=80, null=True , blank=True)
    apdate = models.DateTimeField()
    city = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=60, null=True, blank=True)
    son_name = models.CharField(max_length=80)
    writer = models.CharField(max_length=80)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

