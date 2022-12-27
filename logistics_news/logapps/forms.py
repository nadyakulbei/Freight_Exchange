from .models import Loads
from django.forms import ModelForm, TextInput, Select


class LoadsForm(ModelForm):
    class Meta:
        model = Loads
        fields = ["title", "price", "author"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Маршрут перевозки'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ставка за перевозку'
            }),
            "author": Select(attrs={
                 'class': 'form-control',
                          'placeholder': 'Грузовладелец'})
        }

