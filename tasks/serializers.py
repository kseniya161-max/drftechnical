from tasks.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор к модели Task"""
    class Meta:
        model = Task
        fields = '__all__'


