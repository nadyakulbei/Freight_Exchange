from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Loads
from .forms import LoadsForm


def index(request):
    load = Loads.objects.all()
    return render(request, 'logapps/index.html', {'title': "Основная страница", 'loads': load})


def about(request):
    return render(request, 'logapps/about.html')


def create(request):
    error = ''
    if request.method =='POST':
        form = LoadsForm(request.POST)
        if form.is_valid():
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

# Create your views here.
