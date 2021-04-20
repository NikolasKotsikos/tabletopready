from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_miniatures, name='miniatures'),
    path('<int:miniature_id>/',
         views.miniature_details, name='miniature_details'),
    path('add_miniature/', views.add_miniature, name='add_miniature'),
    path('add_army/', views.add_army, name='add_army'),
    path('add_gamesystem/', views.add_gamesystem, name='add_gamesystem'),
    path('edit_miniature/<int:miniature_id>/',
         views.edit_miniature, name='edit_miniature'),
    path('edit_army/<int:army_id>/',
         views.edit_army, name='edit_army'),
    path('edit_gamesystem/<int:gamesystem_id>/',
         views.edit_gamesystem, name='edit_gamesystem'),
    path('delete_miniature/<int:miniature_id>/',
         views.delete_miniature, name='delete_miniature'),
    path('delete_army/<int:army_id>/',
         views.delete_army, name='delete_army'),
    path('delete_gamesystem/<int:gamesystem_id>/',
         views.delete_gamesystem, name='delete_gamesystem'),
]
