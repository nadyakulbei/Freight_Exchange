from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            name_company = form.cleaned_data.get('name_company')
            number_tel = form.cleaned_data.get('number_tel')
            Profile.objects.create(user=user, name_company=name_company, number_tel=number_tel)
            messages.success(request, f'Успешно создан новый грузовладелец {user.username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

# Create your views here.
