from django import forms
from cuac_core.wrapped_views import GenericCrispyForm
from . import models

class DateInput(forms.DateInput):
    input_type = 'date'
class BatchForm(GenericCrispyForm, forms.ModelForm):

    class Meta:
        model = models.Batch
        fields = '__all__'
        exclude = ["created"]
        labels ={
            'name': 'Nombre',
            'time': 'Horas',
            'hours_elapsed': 'Horas agotadas',
            'expiration': 'Caducidad',
            'company': 'Cliente',
            'status': 'Estado',
                }
        widgets ={
            'expiration' : DateInput()
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

