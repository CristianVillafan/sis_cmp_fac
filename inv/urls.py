from django.urls import path
from .views import CategoriaView
urlpatterns = [
    path('categoria/', CategoriaView.as_view(), name='categoria_list'),
]