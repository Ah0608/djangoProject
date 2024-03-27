# 自定义登陆类，实现多字段登录


from django.contrib.auth.backends import ModelBackend
from rest_framework import serializers
from django.db.models import Q

from login.models import User


class MyBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username) | Q(email=username))
        except:
            raise serializers.ValidationError({'error':'该用户不存在'})

        if user.check_password(password):
            return user
        else:
            raise serializers.ValidationError({'error': '输入的密码错误'})