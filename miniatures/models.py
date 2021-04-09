from django.db import models
from datetime import datetime


class Manufacturer(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Miniature(models.Model):
    manufacturer = models.ForeignKey('Manufacturer',
                                     null=True, blank=True,
                                     on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    gaming_system = models.CharField(max_length=254)
    army = models.CharField(max_length=254)
    faction = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(default=None)
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
