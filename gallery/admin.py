from django.contrib import admin
from gallery.models import GalleryItem


class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'gamesystem',
        'army',
        'faction',
        'date_added',
        'image',
    )

    ordering = ('date_added',)


admin.site.register(GalleryItem, GalleryAdmin)
