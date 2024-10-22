from django import forms
from .models import Categoria, Noticia, Comentario

class NuevaCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
      

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'cuerpo', 'imagen', 'categoria_noticia']
        # widgets = {
        #     'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        #     'contenido': forms.Textarea(attrs={'class': 'form-control'}),
        #     'categoria': forms.Select(attrs={'class': 'form-control'}),
        # }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

