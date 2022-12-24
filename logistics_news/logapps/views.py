from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Loads
from .forms import LoadsForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView


def index(request):
    load = Loads.objects.all()
    paginator = Paginator(load, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'logapps/index.html', {'page_obj': page_obj,'title': "Основная страница", 'loads': load})


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

# class RegisterUser(CreateView):
#     form_class = UserCreationForm
#     template_name = 'logapps/register.html'
#     succes_url = reverse_lazy('register')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Регистрация")
#         return dict(list(context.items()) + list(c_def.items()))
# Create your views here.
def register(request):
    return render(request, 'logapps/about.html')