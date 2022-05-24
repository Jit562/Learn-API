from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


from .serializers import Employeeserializer, EmployeeserializerHyper
from .models import Employee
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

# from rest_framework.permissions import
#                                        AllowAny,
#                                        IsAdminUser,
#                                        IsAuthenticated, 
#                                        IsAuthenticatedOrReadOnly,
#                                        DjangoModelPermissions,
#                                        DjangoModelPermissionsOrAnonReadOnly,
#                                        DjangoObjectPermissions,
#                                        CustomPermission


from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions,DjangoModelPermissions

from .custompermission import MyPermission

# Create your views here.

# permission user


class EmployeList(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer

    # authentication_classes = [SessionAuthentication]
    # authentication_classes = [BasicAuthentication]

    authentication_classes = [TokenAuthentication]



    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermission]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [DjangoObjectPermissions]

    permission_classes = [MyPermission]





# Hyperlink Create 

class EmployeHy(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeserializerHyper




# Cache use in api
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from rest_framework import mixins, generics


class Employeedetails(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Employee.objects.all()

    serializer_class = Employeeserializer

    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    @method_decorator(cache_page(60*60*2))
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    


class Employeedprofile(mixins.RetrieveModelMixin, generics.GenericAPIView):

    queryset = Employee.objects.all()

    serializer_class = Employeeserializer

    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_headers("Authorization",))
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)




# Use Throttling 


from rest_framework.throttling import AnonRateThrottle, UserRateThrottle , ScopedRateThrottle

from .throtling import *

class Employeth(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
    
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # throttle_classes = [AnonRateThrottle, UserRateThrottle]

    # throttle_classes = [jackthrottling, sackthrottling]

    throttle_classes = [ScopedRateThrottle]

    throttle_scope = 'viewst'