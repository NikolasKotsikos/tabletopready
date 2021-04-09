from django.db import models


class GamingSystem(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254,
                                     null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Miniature(models.Model):
    gaming_system = models.ForeignKey('GamingSystem',
                                     null=True, blank=True,
                                     on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    manufacturer = models.CharField(max_length=254)
    army = models.CharField(max_length=254)
    faction = models.CharField(max_length=254,
                               null=True, blank=True)
    description = models.TextField(default=None)
    date_added = models.DateTimeField(auto_now_add=True)
    model_count = models.IntegerField(default=1)
    in_stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024,
                                null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
