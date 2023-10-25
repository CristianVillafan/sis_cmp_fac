from django import forms
from .models import Proveedor, ComprasEnc

class ProveedorForm(forms.ModelForm):
    email=forms.EmailField(max_length=250)
    class Meta:
        model=Proveedor
        exclude=['um','uc','fm','fc']
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ComprasEncForm(forms.ModelForm):
    fecha_compra=forms.DateInput()
    fecha_factura=forms.DateInput()

    class Meta:
        model=ComprasEnc
        fields=['proveedor','fecha_compra','observacion','n_factura','fecha_factura','subtotal','descuento','total']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fecha_compra'].widget.attrs['readonly']=True
        self.fields['fecha_factura'].widget.attrs['readonly']=True
        self.fields['subtotal'].widget.attrs['readonly']=True
        self.fields['descuento'].widget.attrs['readonly']=True
        self.fields['total'].widget.attrs['readonly']=True