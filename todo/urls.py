from django.urls import path

from .views import TodoAPIView
from .func_api_views import todo_api_view

urlpatterns = [
    path('todo/', TodoAPIView.as_view(), name='todo-api-view'),
    path('todo/<int:id>', TodoAPIView.as_view(), name='todo-api-view-id'),
    path('todo-func/', todo_api_view, name='todo-func-api-view'),
    path('todo-func/<int:pk>', todo_api_view, name='todo-func-api-view-id'),
]