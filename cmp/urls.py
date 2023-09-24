from django.urls import path
from .views import ProveedorView, ProveedorNew, ProveedorEdit, proveedor_inactive

urlpatterns = [
    path('proveedor/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedor/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedor/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedor/inactive/<int:id>', proveedor_inactive, name='proveedor_inactive'),


]