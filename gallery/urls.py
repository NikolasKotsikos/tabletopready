from django.urls import path
from . import views

urlpatterns = [
    path('all_gallery_items/',
         views.all_gallery_items,
         name='all_gallery_items'),
    path('add_gallery_item/',
         views.add_gallery_item,
         name='add_gallery_item'),
    path('edit_gallery_item/<int:gallery_item_id>',
         views.edit_gallery_item,
         name='edit_gallery_item'),
    path('delete_gallery_item/<int:gallery_item_id>',
         views.delete_gallery_item,
         name='delete_gallery_item'),
]
