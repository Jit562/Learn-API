from django.urls import path, include
from jwtauth import views
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router = DefaultRouter()

router.register('EmployeList', views.EmployeList)



urlpatterns = [
    path('',include(router.urls)),
    path('jwttoken/',TokenObtainPairView.as_view()),
    path('jwttokenrefresh/',TokenRefreshView.as_view()),
    path('jwttokenverify/',TokenVerifyView.as_view()),
    

    
]