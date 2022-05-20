from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        
        fields = ['name','email','mobile','city','desc']



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        
        fields = ['name','email','mobile','subject']        
