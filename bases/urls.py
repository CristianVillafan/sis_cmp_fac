from django.urls import path
from bases import views

urlpatterns = [
    path('', views.Home.as_view(), name='home')
]