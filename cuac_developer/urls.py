from django.urls import path
from . import views


app_name = 'cuac_developer'


urlpatterns = [
    path('batchs/', views.BatchList.as_view(), name='batch-list'),
    path('batch', views.BatchCreate.as_view(), name='batch-create'),
    path('batch/<int:pk>/', views.BatchDetail.as_view(), name='batch-detail'),
    path('batch/<int:pk>/update/', views.BatchUpdate.as_view(), name='batch-update'),
    path('batch/<int:pk>/delete/', views.BatchDelete.as_view(), name='batch-delete'),
    path('batch/asjson/', views.BatchListAsJSON.as_view(), name='batch-list-asjson'),
    path('batch/editor/', views.BatchEditor.as_view(), name='batch-editor'),

    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('task', views.TaskCreate.as_view(), name='task-create'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('task/<int:pk>/update/', views.TaskUpdate.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task-delete'),
    path('task/asjson/', views.TaskListAsJSON.as_view(), name='task-list-asjson'),
    path('task/editor/', views.TaskEditor.as_view(), name='task-editor'),

]