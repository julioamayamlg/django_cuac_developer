from django import forms
from cuac_core.wrapped_views import GenericCrispyForm
from django.utils.translation import gettext_lazy as _
from . import models


class BatchForm(GenericCrispyForm, forms.ModelForm):

    class Meta:
        model = models.Batch
        fields = '__all__'
        labels ={
            'name': _('Name'),
            'time': _('Hours'),
            'hours_elapsed': _('Hours elapsed'),
            'created': _('Created'),
            'expiration': _('Expires'),
            'company': _('Client'),
            'active': _('Active'),
            'invoiced': _('Invoiced'),
            'charged': _('Charged'),
                }


class TaskForm(GenericCrispyForm, forms.ModelForm):

    class Meta:
        model = models.Task
        fields = '__all__'
        labels ={
            'title': _('Title'),
            'description': _('Description'),
            'time': _('Hours'),
            'batch': _('Batch'),
            'assignee': _('Assignee'),
                }