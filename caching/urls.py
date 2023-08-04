from django.urls import path

from .views import fragment_cache

urlpatterns = [
    path('fragment-cache/', fragment_cache)
]
