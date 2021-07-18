from django.shortcuts import render
from .models import Student

from .forms import StudentForm

from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm

# Create your views here.
from django.http import HttpResponse, Http404


class create(CreateView):

    model = Student

    form_class = StudentForm

    template_name = 'create.html'

    success_url = '/student'

class delete(DeleteView):

    model = Student

    template_name = 'delete.html'

    success_url = '/student'

class update(UpdateView):

    model = Student

    form_class = StudentForm

    template_name = 'update.html'

    success_url = '/student'

class detailView(DetailView):

    model = Student

    template_name = 'detailView.html'


class listView(ListView):

    model = Student

    template_name = 'listView.html'