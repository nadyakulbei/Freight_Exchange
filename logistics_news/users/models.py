from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_company = models.CharField('Стоимость перевозки', max_length=20)
    number_tel = models.CharField('Стоимость перевозки', max_length=20)

    def __str__(self):
        return f'{self.user.username} Profile'
# Create your models here.
