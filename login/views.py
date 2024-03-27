import re

from rest_framework import status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView
from login.models import User
from login.permissions import UserPermission
from login.serializer import UserSerializer


class HomeView(APIView):
    Response({'msg':'登陆成功'})

class LoginView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        result = serializer.validated_data
        result['id'] = serializer.user.id
        result['mobile'] = serializer.user.mobile
        result['email'] = serializer.user.email
        result['username'] = serializer.user.username
        result['token'] = result.pop('access')

        return Response(result, status=status.HTTP_200_OK)


class RegisterView(APIView):

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        mobile = request.data.get('mobiel')
        password = request.data.get('password')
        confirm_pwd = request.data.get('confirm_pwd')

        if not all([username, email, password, confirm_pwd]):
            return Response({'error': '所有参数不能为空'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if re.search(r'^[\u4e00-\u9fa5a-zA-Z0-9]{1,30}$', username):
            if User.objects.filter(username=username).exists():
                return Response({'error': '该用户名已存在'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        else:
            return Response({'error': '用户名只能包含汉字、数字和英文'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if re.search('[a-zA-Z]', password) and re.search('\d', password):
            if not 8 <= len(password) <= 16:
                return Response({'error': '密码长度应在8-16之间'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        else:
            return Response({'error': '密码须同时包含至少一个字母和一个数字'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if password != confirm_pwd:
            return Response({'error': '两次输入的密码不一样'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if not re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email):
            return Response({'error': '邮箱格式错误'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if not re.search(r'^1[3-9]\d{9}$',mobile):
            return Response({'error': '手机号格式错误'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        obj = User.objects.create_user(username=username, email=email, password=password)

        return Response({'id': obj.id, 'username': username, 'email': email}, status=status.HTTP_201_CREATED)


class UserView(GenericViewSet,mixins.RetrieveModelMixin):
    """用户相关操作视图集"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # 设置认证用户才有访问权限
    permission_classes = [IsAuthenticated,UserPermission]
