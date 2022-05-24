from django.db import router
from django.urls import path, include
from classapi import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('studentmd', views.studentmodel)



urlpatterns = [
    path('',include(router.urls)),
    path('student/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.StudentDetails.as_view()),
    path('studentapi/', views.StudentGeneric.as_view()),
    path('studentapi/<int:pk>/', views.StudentGenericdet.as_view()),
    path('studentmax/', views.mixstudentlist.as_view()),
    path('studentmax/<int:pk>/', views.mixistudentdet.as_view()),

    
]
