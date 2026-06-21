import os
from urllib.parse import urlparse

import requests
from django.core.exceptions import MultipleObjectsReturned
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    help = 'Загружает локацию из JSON-файла по указанному адресу'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='Адрес JSON-файла с описанием локации')

    def handle(self, *args, **options):
        url = options['url']

        response = requests.get(url)
        response.raise_for_status()
        place_data = response.json()

        try:
            place, created = Place.objects.get_or_create(
                title=place_data['title'],
                defaults={
                    'short_description': place_data.get('description_short', ''),
                    'long_description': place_data.get('description_long', ''),
                    'lat': float(place_data['coordinates']['lat']),
                    'lng': float(place_data['coordinates']['lng']),
                },
            )
        except MultipleObjectsReturned:
            self.stderr.write(self.style.ERROR(
                f'В базе уже несколько локаций с названием "{place_data["title"]}", пропускаю.'
            ))
            return

        if not created:
            self.stdout.write(self.style.WARNING(
                f'Локация "{place.title}" уже есть в базе, пропускаю.'
            ))
            return

        for position, image_url in enumerate(place_data.get('imgs', [])):
            image_response = requests.get(image_url)
            image_response.raise_for_status()

            filename = os.path.basename(urlparse(image_url).path)

            image = Image(place=place, position=position)
            image.image.save(filename, ContentFile(image_response.content), save=True)

        self.stdout.write(self.style.SUCCESS(
            f'Локация "{place.title}" загружена, картинок: {len(place_data.get("imgs", []))}'
        ))