from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Place


def place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

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
        json_dumps_params={'ensure_ascii': False, 'indent': 4},
    )