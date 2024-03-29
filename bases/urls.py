from django.urls import path
from bases import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='bases/login.html'), name='logout'),
    path('sin_privilegios/', views.HomeSinPrivilegios.as_view(), name='sin_privilegios'),
    path('config/', views.Config.as_view(), name='config')
]