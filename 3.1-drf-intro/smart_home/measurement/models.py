from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            unique=True, verbose_name='Название')
    description = models.CharField(
        max_length=255, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    img = models.ImageField(blank=True, null=True, verbose_name='Изображение')
    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name='Температура')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
