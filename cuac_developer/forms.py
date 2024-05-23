from django import forms
from cuac_core.wrapped_views import GenericCrispyForm
from . import models


class BatchForm(GenericCrispyForm, forms.ModelForm):

    class Meta:
        model = models.Batch
        fields = '__all__'


class TaskForm(GenericCrispyForm, forms.ModelForm):

    class Meta:
        model = models.Task
        fields = '__all__'
