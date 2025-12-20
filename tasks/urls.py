from os import path
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from tasks.views import TaskViewSet, task_list

app_name = "tasks"

router = SimpleRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path('', task_list, name='task_list'),
    path('api/', include(router.urls)),
]

