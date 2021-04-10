from django.contrib import admin
from .models import Miniature, GamingSystem, Army


# Register your models here.
class MiniatureAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'gaming_system',
        'army',
        'price',
        'model_count',
        'in_stock',
        'date_added',
        'image',
    )

    ordering = ('date_added',)


class GamingSystemAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ArmyAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Miniature, MiniatureAdmin)
admin.site.register(GamingSystem, GamingSystemAdmin)
admin.site.register(Army, ArmyAdmin)
