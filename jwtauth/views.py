from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


from .serializers import jarwisSerializer
from .models import Jaarwis
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions,DjangoModelPermissions

from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication

# Create your views here.


class EmployeList(viewsets.ModelViewSet):
    queryset = Jaarwis.objects.all()
    serializer_class = jarwisSerializer

    # authentication_classes = [SessionAuthentication]
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]
