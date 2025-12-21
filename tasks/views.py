from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
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

def task_list(request):
    """Получаем все задачи и передаем в шаблон"""
    tasks = Task.objects.all()
    if request.method == 'POST':
        if 'header' in request.POST:  # Проверяем, что это создание задачи
            serializer = TaskSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                return redirect('tasks:task_list')
        elif 'task_id' in request.POST:  # Проверяем, что это изменение статуса задачи
            task_id = request.POST.get('task_id')
            task = Task.objects.get(id=task_id)
            task.completed = not task.completed  # Меняем статус
            task.save()
            return redirect('tasks:task_list')

    return render(request, 'tasks/task_list.html', {'tasks': tasks})
