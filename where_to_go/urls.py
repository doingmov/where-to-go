from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from places.views import index, place_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', index, name='index'),
    path('places/<int:place_id>/', place_details, name='place_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)