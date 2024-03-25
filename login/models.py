from django.db import models
from common.basedb import BaseModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, BaseModel):  # 同时继承AbstractUser表和BaseModel表里的字段

    mobile = models.CharField(max_length=11, default='', verbose_name='手机号')
    avatar = models.ImageField(blank=True, null=True, verbose_name='头像')

    class Meta:
        db_table = 'users'
        verbose_name = '用户表'


class VerifyCode(models.Model):

    mobile = models.CharField(max_length=11, default='', verbose_name='手机号')
    code = models.CharField(max_length=6,verbose_name='验证码')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class Meta:
        db_table = 'verifycode'
        verbose_name = '验证码表'
