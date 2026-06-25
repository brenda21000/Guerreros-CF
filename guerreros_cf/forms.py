from django import forms
from .models import Contacto


# ─────────────────────────────────────────
# FORMULARIO DE CONTACTO
# ─────────────────────────────────────────
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = (
            'nombre',
            'email',
            'telefono',
            'mensaje'
        )

        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Tu nombre completo',
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'tu@email.com',
            }),

            'telefono': forms.TextInput(attrs={
                'placeholder': '+52 246 xxx xxxx',
            }),

            'mensaje': forms.Textarea(attrs={
                'placeholder': 'Escribe tu mensaje aquí...',
                'rows': 5,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Agrega clase CSS automáticamente
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')
