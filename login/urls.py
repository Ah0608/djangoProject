# _*_ coding : utf-8 _*_
# @Time : 2024/3/24 0024 0:06
# @Author :HuangPeng
# @File : urls
# @Project : djangoProject
from django.contrib import admin
from django.urls import path

from login import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('info/',views.Loginview.as_view())
]