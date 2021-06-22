from django.db import models
from django.contrib.auth.models import User
from django.utils import tree

from datetime import datetime

class Task(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)     #
    name            = models.CharField(max_length=64)
    is_completed    = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True, editable=False)               #
    deadline        = models.DateTimeField(blank=True, null=True)
    completed_at    = models.DateTimeField(blank=True, null=True)           #
    remarks         = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ('is_completed', models.F('deadline').desc(nulls_last=True), 'created_at')


    def save(self, *args, **kwargs):
        if self.is_completed and self.completed_at==None:
            self.completed_at = datetime.now()

        return super().save(*args, **kwargs)
        
