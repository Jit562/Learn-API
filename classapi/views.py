import imp
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



# class base api using mixins 


from rest_framework import mixins, generics


class mixstudentlist(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):


    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class mixistudentdet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer                

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self , request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return  self.destroy(request, *args , **kwargs)         






# class base api using generic view

# Generic_method      (generics.CreateAPIView,
#                       generics.DestroyAPIView,
#                       generics.ListAPIView,
#                       generics.UpdateAPIView,
#                       generics.RetrieveAPIView,
#                       generics.RetrieveUpdateAPIView,
#                       generics.RetrieveDestroyAPIView,
#                       generics.ListCreateAPIView,
#                       generics.RetrieveUpdateDestroyAPIView)


class StudentGeneric(generics.ListCreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer                  



class StudentGenericdet(generics.RetrieveUpdateDestroyAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer 



# class base api using model view

from rest_framework import viewsets


class studentmodel(viewsets.ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer




