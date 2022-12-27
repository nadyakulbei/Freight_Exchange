from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Loads
from .forms import LoadsForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    load = Loads.objects.all()
    paginator = Paginator(load, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'logapps/index.html', {'page_obj': page_obj,'title': "Основная страница", 'loads': load})


def about(request):
    return render(request, 'logapps/about.html')

def delete(request):
    return render(request, 'logapps/post-delete.html')

def post_detail(request):
    return render(request, 'logapps/post-detail.html')


def create(request):
    error = ''
    if request.method =='POST':
        form = LoadsForm(request.POST)
        if form.is_valid():
            form.author = request.user
            form.published_date = datetime.now()
            form.save()
            return redirect('/')
        else:
            error = "Груз добавлен не верно"

    form = LoadsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'logapps/create.html', context)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Loads
    template_name = 'logapps/post-delete.html'
    success_url = '/create'

    def test_func(self):
        load = self.get_object()
        if self.request.user == load.author:
            return True
        return False

class NewsUpdateView(UpdateView):
    model = Loads
    template_name = 'create.html'
    form_class = LoadsForm()

