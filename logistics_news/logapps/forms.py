from .models import Loads
from django.forms import ModelForm, TextInput, Textarea


class LoadsForm(ModelForm):
    class Meta:
        model = Loads
        fields = ["title", "price"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Маршрут перевозки'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ставка за перевозку'
            }),
        }

