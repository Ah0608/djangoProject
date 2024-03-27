from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # 判断登录用户是不是超级管理员，是则拥有所用权限
        if request.user.is_superuser:
            return True
        # 不是超级管理员，则判断操作用户和登录用户是否为同一用户
        return obj == request.user