from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        # widgets = {
        #     'nome': forms.TextInput(attrs={'class': 'form-control'}),
        # }