from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from bases.views import SinPrivilegio
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
# Create your views here.
class CategoriaView(SinPrivilegio, generic.ListView):
    permission_required="inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"

class CategoriaNew(SuccessMessageMixin, SinPrivilegio, generic.CreateView):
    permission_required="inv.add_categoria"
    model = Categoria
    template_name="inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    success_message="Categoria creada satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(SuccessMessageMixin, SinPrivilegio, generic.UpdateView):
    permission_required="inv.change_categoria"
    model = Categoria
    template_name="inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    success_message="Categoria editada satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = "inv/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:categoria_list")
    login_url = "bases:login"

class SubCategoriaView(SinPrivilegio, generic.ListView):
    permission_required="inv.view_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"

class SubCategoriaNew(SinPrivilegio, generic.CreateView):
    permission_required="inv.add_subcategoria"
    model = SubCategoria
    template_name="inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class SubCategoriaEdit(SinPrivilegio, generic.UpdateView):
    permission_required="inv.change_subcategoria"
    model = SubCategoria
    template_name="inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
'''class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = SubCategoria
    template_name = "inv/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = "bases:login" '''
@login_required(login_url='/login/')
@permission_required('inv.change_subcategoria', login_url='bases:sin_privilegios')
def subcategoria_inactive(request, id):
    subcategoria = SubCategoria.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"
    if not subcategoria:
        return redirect("inv:subcategoria_list")
    
    if request.method == 'GET':
        contexto = {'obj':subcategoria}

    if request.method == 'POST':
        subcategoria.estado = False
        subcategoria.save()
        messages.success(request, 'Subcategoria inactivada')
        return redirect("inv:subcategoria_list")

    return render(request, template_name,contexto)


class MarcaView(SinPrivilegio, generic.ListView):
    permission_required='inv.view_marca'
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"

class MarcaNew(SinPrivilegio, generic.CreateView):
    permission_required='inv.add_marca'
    model = Marca
    template_name="inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MarcaEdit(SinPrivilegio, generic.UpdateView):
    permission_required='inv.change_marca'
    model = Marca
    template_name="inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_marca', login_url='bases:sin_privilegios')
def marca_inactive(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"
    if not marca:
        return redirect("inv:marca_list")
    
    if request.method == 'GET':
        contexto = {'obj':marca}

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        messages.success(request, 'Marca inactivada')
        return redirect("inv:marca_list")

    return render(request, template_name,contexto)

class UnidadMedidaView(SinPrivilegio, generic.ListView):
    permission_required='inv.view_unidadmedida'
    model = UnidadMedida
    template_name = "inv/unidadmedida_list.html"
    context_object_name = "obj"

class UnidadMedidaNew(SinPrivilegio, generic.CreateView):
    permission_required='inv.add_unidadmedida'
    model = UnidadMedida
    template_name="inv/unidadmedida_form.html"
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:unidad_medida_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class UnidadMedidaEdit(SinPrivilegio, generic.UpdateView):
    permission_required='inv.change_unidadmedida'
    model = UnidadMedida
    template_name="inv/unidadmedida_form.html"
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:unidad_medida_list")

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_unidadmedida', login_url='bases:sin_privilegios')    
def unidad_medida_inactive(request, id):
    unidad_medida = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"
    if not unidad_medida:
        return redirect("inv:unidad_medida_list")
    
    if request.method == 'GET':
        contexto = {'obj':unidad_medida}

    if request.method == 'POST':
        unidad_medida.estado = False
        unidad_medida.save()
        return redirect("inv:unidad_medida_list")

    return render(request, template_name,contexto)

class ProductoView(SinPrivilegio, generic.ListView):
    permission_required='inv.view_producto'
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"

class ProductoNew(SinPrivilegio, generic.CreateView):
    permission_required='inv.add_producto'
    model = Producto
    template_name="inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProductoEdit(SinPrivilegio, generic.UpdateView):
    permission_required='inv.change_producto'
    model = Producto
    template_name="inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_producto', login_url='bases:sin_privilegios')    
def producto_inactive(request, id):
    producto = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"
    if not producto:
        return redirect("inv:producto_list")
    
    if request.method == 'GET':
        contexto = {'obj':producto}

    if request.method == 'POST':
        producto.estado = False
        producto.save()
        return redirect("inv:producto_list")

    return render(request, template_name,contexto)