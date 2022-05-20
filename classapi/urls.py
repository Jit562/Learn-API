from django.urls import path
from classapi import views

urlpatterns = [
    
    path('student/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.StudentDetails.as_view()),
    
]
