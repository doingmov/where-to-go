from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from afisha.views import index
from places.views import place_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('places/<int:place_id>/', place_details, name='place_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)