from .forms import ContactoForm
from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse_lazy

class ContactoUsuario(FormView):
    template_name = 'contacto/contacto.html'
    form_class = ContactoForm

    def form_valid(self, form):
        # Guardar el formulario o realizar la acción necesaria
        form.save()
        # Mostrar el mensaje de éxito
        messages.success(self.request, 'Tu consulta ha sido enviada correctamente.')
        # No redirige inmediatamente, solo muestra el mensaje
        return super().form_valid(form)

    def get_success_url(self):
        # Redirige a la misma página de contacto dentro del espacio de nombres 'contacto'
        return reverse_lazy('contacto:contacto')  # Aquí está la corrección

