from django import forms

from .models import Contacto

class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea(
        attrs={'cols': '5', 'rows': '10', 'class': 'materialize-textarea'},
    ))

    class Meta:
        model = Contacto
        fields = ('nombre', 'email', 'mensaje')