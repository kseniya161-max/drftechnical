from os import path
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from tasks.views import TaskViewSet

app_name = "tasks"

router = SimpleRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
