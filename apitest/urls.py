from django.urls import path
from apitest import views

urlpatterns = [
    
    path('', views.singer_list, name='singer'),
    path('singer/<int:pk>/', views.singer_details),
]
