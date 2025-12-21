from os import path
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from tasks.views import TaskViewSet, task_list, task_detail, task_update

app_name = "tasks"

router = SimpleRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path('', task_list, name='task_list'),
    path('api/', include(router.urls)),
    path('task/<int:task_id>/', task_detail, name='task_detail'),
    path('task/<int:task_id>/edit/', task_update, name='task_update'),

]