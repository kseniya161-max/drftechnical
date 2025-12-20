from django.urls import path, include
from rest_framework.routers import SimpleRouter
from users.views import UserViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
