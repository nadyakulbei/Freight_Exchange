from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Loads(models.Model):
    title = models.CharField('Маршрут перевозки', max_length=30)  #маршрут
    price = models.CharField('Стоимость перевозки', max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Загрузку"
        verbose_name_plural = "Загрузки"