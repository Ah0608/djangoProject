# _*_ coding : utf-8 _*_
# @Time : 2024/3/25 0025 21:31
# @Author :HuangPeng
# @File : basedb
# @Project : djangoProject

from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        abstract = True  # 这是一张抽象模型，在执行迁移文件时，不会在数据库中生成表
        verbose_name_plural = '公共字段表'
        db_table = 'BaseTable'
