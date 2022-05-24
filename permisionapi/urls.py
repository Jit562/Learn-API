from django.urls import path, include
from permisionapi import views
from .auth import CustomAuthToken

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('employee', views.EmployeList)
router.register('EmployeHy', views.EmployeHy)
router.register('Employeth', views.Employeth)



urlpatterns = [
    path('',include(router.urls)),
    path('gettoken/',CustomAuthToken.as_view()),
    path('Employeedetails/',views.Employeedetails.as_view()),
    path('Employeedetails/<int:pk>/',views.Employeedprofile.as_view()),

    
]