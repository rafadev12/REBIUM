from django import forms
from .models import Foto, Categoria

class FotografiaForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['titulo', 'categoria', 'imagen']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']