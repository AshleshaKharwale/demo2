from django.urls import path

from .views import TodoAPIView
from .func_api_views import todo_api_view
from .drf_generic_views import *

urlpatterns = [
    path('todo/', TodoAPIView.as_view(), name='todo-api-view'),
    path('todo/<int:id>/', TodoAPIView.as_view(), name='todo-api-view-id'),
    path('todo-func/', todo_api_view, name='todo-func-api-view'),
    path('todo-func/<int:pk>/', todo_api_view, name='todo-func-api-view-id'),
    path('todo/generics/list/', ListView.as_view(), name='list-api-view'),
    path('todo/generics/list-create/', ListCreateView.as_view(), name='list-create-api-view'),
    path('todo/generics/update/<int:pk>/', UpdateView.as_view(), name='update-api-view'),
    path('todo/generics/retrieve/<int:pk>/', DetailView.as_view(), name='retrieve-api-view'),
    path('todo/generics/create/', CreateView.as_view(), name='create-api-view'),
    path('todo/generics/delete/<int:pk>/', DeleteView.as_view(), name='destroy-api-view'),
    path('todo/generics/detail-update/<int:pk>/', DetailUpdateView.as_view(),
         name='retrieve-update-api-view'),
    path('todo/generics/detail-delete/<int:pk>/', DetailDeleteView.as_view(),
         name='retrieve-destroy-api-view'),
    path('todo/generics/detail-update-delete/<int:pk>/', DetailUpdateDeleteView.as_view(),
         name='retrieve-update-destroy-api-view'),
    path('todo/generics/', GenericListCreateView.as_view(), name='generic-list-create-api-view'),
    path('todo/generics/<int:pk>/', GenericDetailUpdateDeleteView.as_view(),
         name='generic-retrieve-update-destroy-api-view')
]
