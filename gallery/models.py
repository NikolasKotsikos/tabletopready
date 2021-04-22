from django.db import models


class GalleryItem(models.Model):
    name = models.CharField(max_length=254)
    date_added = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024,
                                null=True, blank=True)
    image = models.ImageField(null=False, blank=True)
    gamesystem = models.CharField(max_length=254)
    army = models.CharField(max_length=254)
    faction = models.CharField(max_length=254)
    manufacturer = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_added']
