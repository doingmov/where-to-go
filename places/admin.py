import traceback

from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 0
    fields = ['preview', 'image', 'position']
    readonly_fields = ['preview']

    def preview(self, obj):
        try:
            if not obj.image:
                return '-'
            return format_html(
                '<img src="{}" style="max-height: 200px; width: auto;">',
                obj.image.url,
            )
        except Exception:
            traceback.print_exc()
            return '-'
    preview.short_description = 'Превью'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title', 'lat', 'lng']
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'position']