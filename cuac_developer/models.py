from django.db import models
from django.contrib.auth import get_user_model
from cuac_core.models import Company
from django.utils import timezone
from . import managers

User = get_user_model()


class Batch(models.Model):
    name = models.CharField(max_length=150)
    time = models.IntegerField(default=0)
    hours_elapsed = models.IntegerField(default=0)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    expiration = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
    active = models.BooleanField()
    invoiced = models.BooleanField()
    charged = models.BooleanField()
    objects = managers.BatchManager()

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    time = models.IntegerField(default=0)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User,
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True)
    objects = managers.TaskManager()

    def __str__(self):
        return f'{self.title}'
