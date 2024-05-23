from django.views import generic
from braces.views import LoginRequiredMixin
from . import models, forms


class BatchList(LoginRequiredMixin, generic.ListView):
    model = models.Batch


class BatchDetail(LoginRequiredMixin, generic.DetailView):
    model = models.Batch


class BatchCreate(LoginRequiredMixin, generic.CreateView):
    model = models.Batch
    form_class = forms.BatchForm


class BatchUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.Batch
    form_class = forms.BatchForm


class BatchDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Batch


class TaskList(LoginRequiredMixin, generic.ListView):
    model = models.Task


class TaskDetail(LoginRequiredMixin, generic.DetailView):
    model = models.Task


class TaskCreate(LoginRequiredMixin, generic.CreateView):
    model = models.Task
    form_class = forms.TaskForm


class TaskUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.Task
    form_class = forms.TaskForm


class TaskDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Task