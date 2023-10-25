from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Proveedor, ComprasDet, ComprasEnc
from django.http import HttpResponse
from .forms import ProveedorForm, ComprasEncForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
import json
from bases.views import SinPrivilegio
from inv.models import Producto
import datetime
from django.db.models import Sum

class ProveedorView(SinPrivilegio, generic.ListView):
    permission_required='cmp.view_proveedor'
    model=Proveedor
    template_name= "cmp/proveedor_list.html"
    context_object_name= 'obj'

class ProveedorNew(SinPrivilegio, generic.CreateView):
    permission_required='cmp.add_proveedor'
    model=Proveedor
    template_name='cmp/proveedor_form.html'
    context_object_name="obj"
    form_class=ProveedorForm
    success_url=reverse_lazy('cmp:proveedor_list')

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProveedorEdit(SinPrivilegio, generic.UpdateView):
    permission_required='cmp.change_proveedor'
    model=Proveedor
    template_name='cmp/proveedor_form.html'
    context_object_name='obj'
    form_class=ProveedorForm
    success_url=reverse_lazy('cmp:proveedor_list')

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_producto', login_url='bases:sin_privilegios')
def proveedor_inactive(request, id):
    proveedor=Proveedor.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'cmp/inactivate.html'

    if not proveedor:
        return HttpResponse("Proveedor no existe: "+ str(id))
    
    if request.method == 'GET':
        contexto = {'obj':proveedor}

    if request.method == 'POST':
        proveedor.estado = False
        proveedor.save()
        contexto={'obj':'Ok'}
        return HttpResponse("Proveedor inactivado")
    
    return render(request, template_name, contexto)

class ComprasView(SinPrivilegio, generic.ListView):
    model=ComprasEnc
    template_name='cmp/compras_list.html'
    context_object_name='obj'
    permission_required='cmp.view_comprasenc'

@login_required(login_url='/login/')
@permission_required('cmp.view_comprasenc', login_url='bases:sin_privilegios')
def compras(request, compra_id=None):
    template_name='cmp/compras.html'
    prod=Producto.objects.filter(estado=True)
    form_compras={}
    contexto={}

    if request.method == 'GET':
        form_compras=ComprasEncForm()
        enc=ComprasEnc.objects.filter(pk=compra_id).first()

        if enc:
            det = ComprasDet.objects.filter(compra=enc)
            fecha_compra=datetime.date.isoformat(enc.fecha_compra)
            #fecha_compra = datetime.strptime(fecha_compra, "%Y-%m-%d")
            #fecha_compra = datetime.datetime.strptime(enc.fecha_compra, "%d-%m-%Y").strftime("%YYYY-%mm-%dd")
            fecha_factura=datetime.date.isoformat(enc.fecha_factura)
            #fecha_factura = datetime.strptime(fecha_factura, "%Y-%m-%d")
            #fecha_factura = datetime.datetime.strptime(enc.fecha_factura, "%d-%m-%Y").strftime("%YYYY-%mm-%dd")

            e={
                'fecha_compra':fecha_compra,
                'proveedor': enc.proveedor,
                'observacion': enc.observacion,
                'n_factura': enc.n_factura,
                'fecha_factura':fecha_factura,
                'subtotal': enc.subtotal,
                'descuento': enc.descuento,
                'total': enc.total
            }

            form_compras = ComprasEncForm(e)

        else:
            det=None

        contexto={
            'productos':prod,'encabezado':enc,'detalle':det,'form_enc':form_compras,
        }

    if request.method == 'POST':
        fecha_compra=request.POST.get('fecha_compra')
        observacion=request.POST.get('observacion')
        n_factura=request.POST.get('n_factura')
        fecha_factura=request.POST.get('fecha_factura')
        proveedor=request.POST.get('proveedor')
        subtotal=0
        descuento=0
        total=0

        if not compra_id:
            prov=Proveedor.objects.get(pk=proveedor)
            enc=ComprasEnc(
                fecha_compra=fecha_compra,
                observacion=observacion,
                n_factura=n_factura,
                fecha_factura=fecha_factura,
                proveedor=prov,
                uc=request.user                    
            )
            if enc:
                enc.save()
                compra_id=enc.id
        else:
            enc=ComprasEnc.objects.filter(pk=compra_id).first()
            if enc:
                enc.fecha_compra=fecha_compra,
                enc.observacion=observacion,
                enc.n_factura=n_factura,
                enc.fecha_factura=fecha_compra,
                enc.um=request.user.id
                enc.save()

        if not compra_id:
            return redirect('cmp:compras_list')
        
        producto=request.POST.get('id_id_producto')
        cantidad=request.POST.get('id_cantidad_detalle')
        precio=request.POST.get('id_precio_detalle')
        subtotal_detalle=request.POST.get('id_subtotal_detalle')
        descuento_detalle=request.POST.get('id_descuento_detalle')
        total_detalle=request.POST.get('id_total_detalle')

        prod=Producto.objects.get(pk=producto)

        det=ComprasDet(
            compra=enc,
            producto=prod,
            cantidad=cantidad,
            precio_prv=precio,
            descuento=descuento_detalle,
            uc=request.user
        )
        if det:
            det.save()

            #subtotal=ComprasDet.objects.filter(compra=compra_id).aaggregate(Sum('subtotal'))
            subtotal = ComprasDet.objects.filter(compra=compra_id).aggregate(subtotal=Sum('subtotal')).get('subtotal',0.00)
            #descuento=ComprasDet.objects.filter(compra=compra_id).aaggregate(Sum('descuento'))
            descuento = ComprasDet.objects.filter(compra=compra_id).aggregate(descuento=Sum('descuento')).get('descuento',0.00)
            #enc.subtotal=subtotal['subtotal__sum']
            enc.subtotal=subtotal
            #enc.descuento=descuento['descuento__sum']
            enc.descuento=descuento
            enc.save()

        return redirect('cmp:compras_edit', compra_id=compra_id)
            

    return render(request,template_name,contexto)