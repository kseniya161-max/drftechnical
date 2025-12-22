from django.db import models

class Task(models.Model):
    """Модель Задачи"""
    header = models.CharField(max_length=150, verbose_name='заголовок')
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header


