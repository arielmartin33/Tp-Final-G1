from django import forms
from .models import Categoria, Noticia

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        # widgets = {
        #     'nome': forms.TextInput(attrs={'class': 'form-control'}),
        # }

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'cuerpo', 'imagen', 'categoria_noticia']
        # widgets = {
        #     'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        #     'contenido': forms.Textarea(attrs={'class': 'form-control'}),
        #     'categoria': forms.Select(attrs={'class': 'form-control'}),
        # }