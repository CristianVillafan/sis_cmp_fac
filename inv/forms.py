from django import forms
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion','estado']
        labels = {'descripcion':'Descipcion de la categoria','estado':'Estado'}
        widget = {'descripcion': forms.TextInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset= Categoria.objects.filter(estado=True)

    )
    class Meta:
        model = SubCategoria
        fields = ['categoria','descripcion','estado']
        labels = {'categoria':'Categoria','descripcion':'Descripcion de la sub categoria','estado':'Estado'}
        widget = {'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['categoria'].empty_label = "Seleccione categoria"

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['descripcion','estado']
        labels = {'descripcion':'Descipcion de la categoria','estado':'Estado'}
        widget = {'descripcion': forms.TextInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['descripcion','estado']
        labels = {'descripcion':'Descripcion de la unidad de medida','estado':'Estado'}
        widget = {'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['codigo','codigo_barra', 'descripcion', 'estado', 'precio', 'existencia', 'ultima_compra', 'marca', 'subcategoria', 'unidad_medida']
        exclude=['um','fm','uc','fc']
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly']=True
        self.fields['existencia'].widget.attrs['readonly']=True