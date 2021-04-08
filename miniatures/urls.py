from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_miniatures, name='miniatures'),
    path('<miniature_id>', views.miniature_details, name='miniature_details'),
]
