from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task_list_create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task_retrieve_update_destroy'),
]
