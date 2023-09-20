from django.urls import path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel, MarcaView, MarcaNew, MarcaEdit , marca_inactive, UnidadMedidaView, UnidadMedidaNew, UnidadMedidaEdit, unidad_medida_inactive
urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDel.as_view(), name= 'categoria_del'),

    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategoria/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/delete/<int:pk>', SubCategoriaDel.as_view(), name= 'subcategoria_del'),

    path('marcas/', MarcaView.as_view(), name='marca_list'),
    path('marcas/new', MarcaNew.as_view(), name='marca_new'),
    path('marcas/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),
    path('marcas/inactive/<int:id>', marca_inactive , name='marca_inactive'),

    path('unidades_de_medida', UnidadMedidaView.as_view(), name='unidad_medida_list'),
    path('unidades_de_medida/new', UnidadMedidaNew.as_view(), name = 'unidad_medida_new'),
    path('unidades_de_medida/edit/<int:pk>', UnidadMedidaEdit.as_view(), name='unidad_medida_edit'),
    path('unidades_de_medida/inactive/<int:id>', unidad_medida_inactive , name='unidad_medida_inactive'),



]