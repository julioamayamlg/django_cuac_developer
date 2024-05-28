from django.views import generic
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin, PermissionRequiredMixin, JSONResponseMixin
from cuac_core.mixins import DatatableListView, DatatableEditor
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from . import models, forms


class BatchList(LoginRequiredMixin, generic.ListView):
    model = models.Batch

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'breadcrumb_list': [
                {'label': 'Lotes',
                 'url': reverse_lazy('cuac_core:batch-list')}
            ]})
        return context

class BatchDetail(LoginRequiredMixin, generic.DetailView):
    model = models.Batch

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.object.name,
            'breadcrumb_list': [
                {'label': 'Lotes',
                 'url': reverse_lazy('cuac_developer:batch-list')},
                {'label': self.object.name}
            ]})
        return context

class BatchCreate(LoginRequiredMixin, generic.CreateView):
    model = models.Batch
    form_class = forms.BatchForm

    def get_success_url(self):
        return reverse_lazy('cuac_developer:batch-list')


class BatchUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.Batch
    form_class = forms.BatchForm


class BatchDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Batch


class BatchEditor(LoginRequiredMixin,
                    DatatableEditor):
    model = models.Batch


class TaskList(LoginRequiredMixin, generic.ListView):
    model = models.Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'breadcrumb_list': [
                {'label': 'Tareas',
                 'url': reverse_lazy('cuac_developer:task-list')}
            ]})
        return context

class TaskDetail(LoginRequiredMixin, generic.DetailView):
    model = models.Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.object.title,
            'breadcrumb_list': [
                {'label': 'Tareas',
                 'url': reverse_lazy('cuac_developer:task-list')},
                {'label': self.object.title}
            ]})
        return context


class TaskCreate(LoginRequiredMixin, generic.CreateView):
    model = models.Task
    form_class = forms.TaskForm

    def get_success_url(self):
        return reverse_lazy('cuac_developer:task-list')

class TaskUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.Task
    form_class = forms.TaskForm


class TaskDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Task


class TaskEditor(LoginRequiredMixin,
                    DatatableEditor):
    model = models.Task


class TaskListAsJSON(LoginRequiredMixin, DatatableListView):
    model = models.Task
    column_names_map = {
    }

    @staticmethod
    def get_actions(obj):
        return (f"<a href='{reverse_lazy('cuac_developer:task-detail', kwargs={'pk': obj.pk})}' "
                f"class='btn btn-primary'>"
                f"<i class='bi bi-eye'></i>"
                f"</a>")

    def object_wrapper(self, obj):
        row = {
            'DT_RowId': obj.pk,
            'title': obj.title,
            'description': obj.description,
            'time': obj.time,
            'batch': obj.batch.name,
            'assignee': obj.assignee.pk,
            'assignee_name': obj.assignee.first_name,
            'actions': f'<div class="btn-group">{self.get_actions(obj)}</div>'
        }
        return row


class BatchListAsJSON(LoginRequiredMixin, DatatableListView):
    model = models.Batch
    column_names_map = {
    }

    @staticmethod
    def get_actions(obj):
        return (f"<a href='{reverse_lazy('cuac_developer:batch-detail', kwargs={'pk': obj.pk})}' "
                f"class='btn btn-primary'>"
                f"<i class='bi bi-eye'></i>"
                f"</a>")

    def object_wrapper(self, obj):
        row = {
            'DT_RowId': obj.pk,
            'name': obj.name,
            'time': obj.time,
            'hours_elapsed': obj.hours_elapsed,
            'created': obj.created,
            'expiration': obj.expiration,
            'company_pk': obj.company.pk,
            'company': obj.company.name,
            'active': obj.active,
            'invoiced': obj.invoiced,
            'charged': obj.charged,
            'actions': f'<div class="btn-group">{self.get_actions(obj)}</div>'
        }
        return row
