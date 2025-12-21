from os import path
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from tasks.views import TaskViewSet, task_list, create_task

app_name = "tasks"

router = SimpleRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', create_task, name='task_create'),
    path('api/', include(router.urls)),
]