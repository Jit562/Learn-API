from os import stat
from django.shortcuts import render
from classapi import serializers

from classapi.serializers import StudentSerializer, TeacherSerializer
from classapi.models import Student, Teacher
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class StudentList(APIView):
    def get(self, request, format=None):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        



class StudentDetails(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format= None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student =self.get_object(pk)
        serializers = StudentSerializer(student, data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk, format=None):
        student = self.get_object(pk) 
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                         