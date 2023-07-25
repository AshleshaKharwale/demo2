from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


# @login_required(login_url='/admin')
# def welcome(request):
#     return HttpResponse("Welcome!")


class WelcomeView(LoginRequiredMixin, TemplateView):
    template_name = "home/welcome.html"
    login_url = "/admin"


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    success_url = '/notes/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponse("<h1>You are already logged in!</h1>")
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class SignupInterfaceView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'home/signup.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponse("<h1>You are already logged in!</h1>")
        return super().get(request, *args, **kwargs)
