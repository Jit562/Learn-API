from django.urls import path
from apitest import views

urlpatterns = [
    
    path('', views.singer_list, name='singer'),
    path('singer/<int:pk>/', views.singer_details),
    path('sing/', views.singerlist, name='sing'),
    path('sing/<int:pk>/', views.singerdetails),
    path('song/', views.songlist, name='song'),
]
