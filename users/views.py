from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """ Представление для Пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

def login_view(request):
    """Представление для авторизации пользователя"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tasks:task_list')
        else:
            print("Authentication failed!")
            return render(request, 'users/login.html', {'error': 'Неверное имя пользователя или пароль'})
    return render(request, 'users/login.html', {})


def registration_view(request):
    """Представление для регистрации пользователя"""
    if request.method == 'POST':
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.POST['password'])
            user.save()
            return redirect('users:login')
    return render(request, 'users/registration.html', {})


def logout_view(request):
    """Представление для выхода пользователя"""
    logout(request)
    return redirect('users:login')