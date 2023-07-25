from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import NotesModel

# Create your views here.

# def listnotes(request):
#     notes = NotesModel.objects.all()
#     return render(request, "notes/notes_list.html", {"notes": notes})


class NotesListView(LoginRequiredMixin, ListView):
    model = NotesModel
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

# def listdetail(request, id):
#     try:
#         note = NotesModel.objects.get(id=id)
#     except:
#         raise Http404("Id does not exist")
#     return render(request, "notes/notes_detail.html", {"note": note})


class NotesDetailView(LoginRequiredMixin, DetailView):
    model = NotesModel
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'
    login_url = '/login'


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = NotesModel
    fields = '__all__'
    success_url = '/notes/'
    login_url = '/login'


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = NotesModel
    fields = '__all__'
    success_url = '/notes/'
    login_url = '/login'


class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = NotesModel
    success_url = '/notes/'
    login_url = '/login'