from django import forms
from cuac_core.wrapped_views import GenericCrispyForm
from django.contrib.admin import widgets
from . import models


class BatchForm(GenericCrispyForm, forms.ModelForm):

    class Meta:
        model = models.Batch
        fields = '__all__'
        labels ={
            'name': 'Nombre',
            'time': 'Horas',
            'hours_elapsed': 'Horas agotadas',
            'created': 'Creado',
            'expiration': 'Caducidad',
            'company': 'Cliente',
            'active': 'Activo',
            'invoiced': 'Facturado',
            'charged': 'Cobrado',
                }
        widgets ={
            'created' : widgets.AdminSplitDateTime(),
            'expiration' : widgets.AdminSplitDateTime()
        }


class TaskForm(GenericCrispyForm, forms.ModelForm):

    class Meta:
        model = models.Task
        fields = '__all__'
        labels ={
            'title': 'Tarea',
            'description': 'Descripción',
            'time': 'Horas',
            'batch': 'Lote',
            'assignee': 'Asignado',
                }