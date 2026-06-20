from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = models.TextField('Длинное описание', blank=True)
    lat = models.FloatField('Широта')
    lng = models.FloatField('Долгота')

    def __str__(self):
        return self.title