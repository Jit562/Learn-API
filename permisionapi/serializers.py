from rest_framework import serializers
from .models import Employee


class Employeeserializer(serializers.ModelSerializer):

    class Meta:
        model = Employee

        fields = ['id','name','email','mobile','desc','bool','date']





# Hyperlinkserializer create

class EmployeeserializerHyper(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee

        fields = ['url','id','name','email','mobile','desc','bool','date']