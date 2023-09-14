from django.urls import path
from bases import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'), name='login'),
]