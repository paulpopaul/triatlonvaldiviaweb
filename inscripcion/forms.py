# coding=utf-8
from django import forms

from .models import *


class PersonaForm(forms.ModelForm):
    rut = forms.CharField(max_length=15, help_text='12345678-5', error_messages={'required': 'Porfavor sin puntos ni guión'})
    nombre = forms.CharField(max_length=16, error_messages={'required': 'Ingrese su nombre'})
    apellido_pat = forms.CharField(max_length=16)
    apellido_mat = forms.CharField(max_length=16)
    sexo = forms.Select(choices=CHOICES_SEXO, )
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date',
                                                                     'class': 'datepicker',
                                                                     }), )
    telefono = forms.CharField(max_length=16)
    celular = forms.CharField(max_length=16)
    comuna = forms.CharField(max_length=16)
    direccion = forms.CharField(max_length=64)
    club = forms.CharField(max_length=32)
    talla_polera = forms.Select(choices=CHOICES_TALLA, )
    medio_pago = forms.Select(choices=CHOICES_PAGO, )


    class Meta:
        model = Persona
        fields = ('rut', 'nombre', 'apellido_pat', 'apellido_mat', 'sexo', 'email', 'fecha_nacimiento',
                  'telefono', 'celular', 'comuna', 'direccion', 'club', 'nacionalidad',
                  'talla_polera', 'medio_pago', 'edad_y_precio')

