from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def index(request):
    places = Place.objects.all()

    context = {
        'places': {
            'type': 'FeatureCollection',
            'features': [
                {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [place.lng, place.lat],
                    },
                    'properties': {
                        'title': place.title,
                        'placeId': place.id,
                        'detailsUrl': reverse(
                            'place_details',
                            kwargs={'place_id': place.id}
                        ),
                    },
                }
                for place in places
            ]
        }
    }

    return render(request, 'index.html', context)


def place_details(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related('images'),
        pk=place_id
    )

    serialized_place = {
        'title': place.title,
        'imgs': [
            request.build_absolute_uri(image.image.url)
            for image in place.images.all()
        ],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng,
        },
    }

    return JsonResponse(
        serialized_place,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 4,
        },
    )