from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = models.TextField('Длинное описание', blank=True)
    lat = models.FloatField('Широта')
    lng = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name='Место',
    )
    image = models.ImageField('Изображение', upload_to='places')
    position = models.IntegerField('Порядок', default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.place.title} — фото №{self.position}'