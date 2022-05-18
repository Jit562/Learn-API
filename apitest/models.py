from csv import writer
from django.db import models

# Create your models here.


class Singer(models.Model):
    
    name = models.CharField(max_length=80, null=True , blank=True)
    
    gender = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=60, null=True, blank=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')
    duration = models.IntegerField()

    def __str__(self):
        return self.title

