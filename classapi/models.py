from pyexpat import model
from django.db import models

# Create your models here.

class Commonbase(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)
    mobile = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(max_length=70)
    boolean = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


class Student(Commonbase):
    city = models.CharField(max_length=60)
    desc = models.TextField()
    
    def __str__(self):
        return self.name



class Teacher(Commonbase):
    subject = models.CharField(max_length=80)
   
    def __str__(self):
        return self.name        
