from django import forms
from.models import Contacto

class ContactoForm (forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_apellido', 'email', 'asunto', 'mensaje']


# from django import forms

# class ContactoForm(forms.Form):
    # nombre = forms.CharField(max_length=100)
    # email = forms.EmailField()
    # mensaje = forms.CharField(widget=forms.Textarea)
