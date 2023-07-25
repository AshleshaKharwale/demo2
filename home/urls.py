from django.urls import path
from .views import *

urlpatterns = [
    path('welcome/', WelcomeView.as_view()),
    path('login/', LoginInterfaceView.as_view(), name='login'),
    path('logout/', LogoutInterfaceView.as_view(), name='logout'),
    path('signup/', SignupInterfaceView.as_view(), name='signup')
]
