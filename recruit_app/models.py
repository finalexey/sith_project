from django.db import models


class Planet(models.Model):

    name = models.CharField(
        max_length=32,
        verbose_name='Планета')

    def __str__(self):
        return self.name


class Sith(models.Model):

    name = models.CharField(
        max_length=32,
        verbose_name='Имя Ситха')

    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Планета')

    def __str__(self):
        return self.name


class Recruit(models.Model):

    name = models.CharField(
        max_length=32,
        verbose_name='Имя Рекрута')

    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Планета')

    age = models.IntegerField(
        verbose_name='Возраст')

    email = models.EmailField(
        verbose_name='Email',
        unique=True)

    is_accepted = models.BooleanField(
        verbose_name='Принят ли рекрут', default=False)

    def __str__(self):
        return self.name
