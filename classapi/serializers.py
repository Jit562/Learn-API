from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        
        fields = ['id','name','email','mobile','city','desc']



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        
        fields = ['id','name','email','mobile','subject']        
