from os import path

from rest_framework.routers import SimpleRouter

from tasks.views import TaskViewSet

app_name = "tasks"

router = SimpleRouter()
router.register(r"tasks", TaskViewSet)


urlpatterns = [
    path("task/", TaskViewSet.as_view(), name="task"),
]
urlpatterns += router.urls
