from django.db import models

class Loads(models.Model):
    title = models.CharField('Маршрут перевозки', max_length=30)  #маршрут
    price = models.CharField('Стоимость перевозки', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Загрузку"
        verbose_name_plural = "Загрузки"