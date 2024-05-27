from django.views import generic
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin, PermissionRequiredMixin, JSONResponseMixin
from cuac_core.mixins import DatatableListView, DatatableEditor
from django.urls import reverse_lazy
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


class BatchEditor(LoginRequiredMixin,
                    DatatableEditor):
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


class TaskEditor(LoginRequiredMixin,
                    DatatableEditor):
    model = models.Task


class TaskListAsJSON(LoginRequiredMixin, DatatableListView):
    model = models.Task
    column_names_map = {
    }

    @staticmethod
    def get_actions(obj):
        return (f"<a href='{reverse_lazy('cuac_core:task-detail', kwargs={'pk': obj.pk})}' "
                f"class='btn btn-primary'>"
                f"<i class='bi bi-eye'></i>"
                f"</a>"
                f"<a href='{reverse_lazy('cuac_core:task-delete', kwargs={'pk': obj.pk})}' "
                f"class='btn btn-danger'>"
                f"<i class='bi bi-trash'></i>"
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
        }
        return row


class BatchListAsJSON(LoginRequiredMixin, DatatableListView):
    model = models.Batch
    column_names_map = {
    }

    @staticmethod
    def get_actions(obj):
        return (f"<a href='{reverse_lazy('cuac_core:batch-detail', kwargs={'pk': obj.pk})}' "
                f"class='btn btn-primary'>"
                f"<i class='bi bi-eye'></i>"
                f"</a>"
                f"<a href='{reverse_lazy('cuac_core:batch-delete', kwargs={'pk': obj.pk})}' "
                f"class='btn btn-danger'>"
                f"<i class='bi bi-trash'></i>"
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
        }
        return row
