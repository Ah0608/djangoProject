# _*_ coding : utf-8 _*_
# @Time : 2024/3/24 0024 0:06
# @Author :HuangPeng
# @File : urls
# @Project : djangoProject

from django.contrib import admin
from django.urls import path
from login import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    # token的刷新和验证
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('token/verify/',TokenVerifyView.as_view(),name='token_verify'),
    path('users/<str:pk>/',views.UserView.as_view({'get':'retrieve'}),name='users'),
]
