from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_miniatures, name='miniatures'),
    path('<int:miniature_id>/',
         views.miniature_details, name='miniature_details'),
    path('add_miniature/', views.add_miniature, name='add_miniature'),
    path('add_army/', views.add_army, name='add_army'),
    path('add_gamesystem/', views.add_gamesystem, name='add_gamesystem'),
]
