from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Proveedor
from django.http import HttpResponse
from .forms import ProveedorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
import json

class ProveedorView(LoginRequiredMixin, generic.ListView):
    model=Proveedor
    template_name= "cmp/proveedor_list.html"
    context_object_name= 'obj'
    login_url='bases:login'

class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model=Proveedor
    template_name='cmp/proveedor_form.html'
    context_object_name="obj"
    form_class=ProveedorForm
    success_url=reverse_lazy('cmp:proveedor_list')
    login_url='bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
    model=Proveedor
    template_name='cmp/proveedor_form.html'
    context_object_name='obj'
    form_class=ProveedorForm
    success_url=reverse_lazy('cmp:proveedor_list')
    login_url='bases_login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def proveedor_inactive(request, id):
    proveedor=Proveedor.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'cmp/inactivate.html'

    if not proveedor:
        return HttpResponse("Proveedor no existe"+ str(id))
    
    if request.method == 'GET':
        contexto = {'obj':proveedor}

    if request.method == 'POST':
        proveedor.estado = False
        proveedor.save()
        contexto={'obj':'Ok'}
        return HttpResponse("Proveedor inactivado")

    return render(request, template_name, contexto)
# Create your views here.
