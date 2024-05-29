from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel, ActivatorModel
from django.contrib.auth import get_user_model
from cuac_core.models import Company
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from . import managers

User = get_user_model()


class Batch(TitleDescriptionModel, ActivatorModel):
    #class BatchStatus(models.TextChoices):
    #    ACTIVE = "active", _("Active")
    #    BILLED = "billed", _("Billed")
    #    CHARGED = "charged", _("Charged")

    name = models.CharField(max_length=150)
    time = models.IntegerField(default=0)
    hours_elapsed = models.IntegerField(default=0)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    expiration = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)

    active = models.BooleanField()
    invoiced = models.BooleanField()
    charged = models.BooleanField()

    #status = models.CharField(choices=BatchStatus, default=BatchStatus.ACTIVE)
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
