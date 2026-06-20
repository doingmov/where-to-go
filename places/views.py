from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Place


def place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return HttpResponse(place.title)
