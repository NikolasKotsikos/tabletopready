from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=200)
    state = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Miniature(models.Model):
    name = models.CharField(max_length=200)
    subcategory = models.ForeignKey(Subcategory,
                                    unique=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True,
                                 default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
