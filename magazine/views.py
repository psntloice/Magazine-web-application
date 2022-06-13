from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
#connects to the home template

class Homepage(ListView):
    model =Post
    template_name = 'magazine/home.html'
    fields = ['title', 'author', 'body']#check
    context_object_name = 'object_list'#check
#def homepage(request):
 #   return render(request, 'magazine/home.html')

def aboutpage(request):
    return render(request, 'magazine/about.html')


class Getdetail(DetailView):
    model=Post
    template_name = 'magazine/thedetail.html'

class Createnew(CreateView):
    model =Post
    template_name = 'magazine/new.html'
    fields = ['the_text', 'author', 'body']


class Editt(UpdateView):
    model=Post
    template_name = 'magazine/edit.html'
    fields = ['the_text', 'body']

class Delette(DeleteView):
    model=Post
    template_name = 'magazine/delete.html'
    success_url = reverse_lazy('home')