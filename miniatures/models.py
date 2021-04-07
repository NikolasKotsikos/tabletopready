from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(default=None)
        
    def __str__(self):
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    
    def get_friendly_name(self):
        return self.friendly_name
    
    class Meta:
        # enforcing that there can not be two categories under a parent with the same slug
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"


class Miniature(models.Model):
    category = models.ForeignKey(Category, blank=True,
                                 default=None, on_delete=models.CASCADE)    
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateField(auto_now=False, auto_now_add=True) 
    slug = models.SlugField(default=None, unique=True)       

    def __str__(self):
        return self.name
    
    def get_cat_list(self):
        k = self.category
        
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]
