from django.db import models
from bases.models import ClaseModelo
from inv.models import Producto

# Create your models here.
class Proveedor(ClaseModelo):
    descripcion=models.CharField(max_length=100, unique=True)
    direccion=models.CharField(max_length=250, null=True, blank=True)
    contacto=models.CharField(max_length=100)
    telefono=models.CharField(max_length=10, null=True, blank=True)
    email=models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return {}.format(self.descripcion)
    
    def save(self):
        self.descripcion=self.descripcion.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural = "Proveedores"

class ComprasEnc(ClaseModelo):
    fecha_compra=models.DateField(null='True',blank='True')
    observacion=models.TextField(null='True', blank='True')
    n_factura=models.CharField(max_length=100)
    fecha_factura=models.DateField(null=True, blank=True)
    subtotal=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.observacion)
    
    def save(self):
        self.observacion=self.observacion.upper()
        self.total=self.subtotal-self.descuento
        super(ComprasEnc, self).save()

    class Meta:
        verbose_name_plural= 'Encabezado compras'
        verbose_name= 'Encabezado compra'

class ComprasDet(ClaseModelo):
    compra=models.ForeignKey(ComprasEnc, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad=models.BigIntegerField(default=0)
    precio_prv=models.FloatField(default=0)
    subtotal=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)
    costo=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.subtotal=float(float(int(self.cantidad))*float(self.precio_prv))
        self.total=self.subtotal-float(self.descuento)
        super(ComprasDet, self).save()

    class Meta:
        verbose_name_plural='Detalle compras'
        verbose_name='Detalle compra'
