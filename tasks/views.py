from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_delete(self, serializer):
        serializer.save()

    def retrieve(self, request, *args, **kwargs):
        """Получение задачи по ID"""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

def task_list(request):
    """Получаем, удаляем, создаем все задачи и передаем в шаблон"""
    tasks = Task.objects.all()
    if request.method == 'POST':
        if 'header' in request.POST:
            serializer = TaskSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                return redirect('tasks:task_list')
        elif 'task_id' in request.POST:
            task_id = request.POST.get('task_id')
            task = Task.objects.get(id=task_id)
            if 'delete_task' in request.POST:
                task.delete()
            else:
                task.completed = not task.completed
                task.save()
            return redirect('tasks:task_list')

    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_detail(request, task_id):
    """Получаем задачу по ID и передаем в шаблон"""
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})
