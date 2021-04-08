from django.contrib import admin
from .models import Miniature, Manufacturer


# Register your models here.
class MiniatureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'gaming_system',
        'faction',
        'price',
        'date_added',
        'image',
    )

    ordering = ('date_added',)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Miniature, MiniatureAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
