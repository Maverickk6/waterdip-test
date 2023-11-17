from django.db import models

# Create your models here.

class TaskModel(models.Model):
    title = models.CharField(max_length=300)
    is_completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title