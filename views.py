# coding=utf-8
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from contacto.forms import ContactoForm
from inscripcion.forms import PersonaForm
from hoteles.models import Dato
from django.core.mail import send_mail  # Create your views here.
from inscripcion.models import Persona

from django.core.mail import EmailMultiAlternatives

def index(request):
    if request.method == "POST":
        contact = ContactoForm(request.POST)
        mensaje_enviado = '/enviando/'
        if contact.is_valid():
            c = contact.save(commit=False)
            c.save()
            to_mail = c.email
            subject, from_email, to = 'Copia Mensaje TrirotaryValdivia', 'noresponder@trirotaryvaldivia.cl', to_mail,
            text_content = 'Gracias por inscribirte'
            html_content = '<h1>Copia del mensaje en trirotaryvaldivia.cl:</h1><br><p><strong>Mensaje: </strong><br>'+c.mensaje+'</p><br><p><strong>De: </strong>'+c.nombre+'('+c.email+')</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            to_mail = 'contacto@trirotaryvaldivia.cl'
            subject, from_email, to = 'Copia Mensaje TrirotaryValdivia', 'noresponder@trirotaryvaldivia.cl', to_mail,
            text_content = 'Gracias por inscribirte'
            html_content = '<h1>Copia del mensaje en trirotaryvaldivia.cl:</h1><br><p><strong>Mensaje: </strong><br>'+c.mensaje+'</p><br><p><strong>De: </strong>'+c.nombre+'('+c.email+')</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            print('Enviado :v')
            return redirect(mensaje_enviado)
    else:
        contact = ContactoForm()
    hoteles = Dato.objects.filter(tipo='HOTEL')
    otros = Dato.objects.exclude(tipo='HOTEL')
    context = {
        'hoteles': hoteles,
        'otros': otros,
        'form': contact,
    }
    return render(request, 'web/index.html', context)


def inscripcion(request):
    print('Empieza..')
    if request.method == "POST":
        print('Posteando')
        form = PersonaForm(request.POST)
        redireccion = '/enviando/'
        if form.is_valid():
            print('Valido')
            c = form.save(commit=False)
            c.save()
            print('guardado')
            to_mail = c.email
            subject, from_email, to = 'Email Confirmación TrirotaryValdivia', 'noresponder@trirotaryvaldivia.cl', to_mail
            text_content = 'Gracias por inscribirte'
            html_content = '<div style="background-color: #0D1422; color: #fff; text-align: center; font-family:Helvetica; padding: 50px; "> <h1>Estamos registrando su inscripción</h1> <p>Pronto sus datos serán revisados y podrá revisarlos haciendo click <a style="color: #ff0" href="http://trirotaryValdivia.cl/listado-inscritos/">aquí</a></p> <p>El triatlón se realizará el día 18 de Febrero del 2017</p> <p>Para mayor información visite <a style="color: #ff0" href="http://trirotaryValdivia.cl/">TrirotaryValdivia</a> para tener las ultimas novedades</p> <p>Para la realización de transferencias electrónicas los datos son los siguientes:</p> <p> Banco de Chile<br> Cuenta Corriente<br> N° : 251-0141010<br> A nombre de ROTARY CLUB VALDIVIA<br> Rut: 65.117.561-5<br> </p> <p> Email<br> contacto@trirotaryvaldivia.cl<br> </p> <p> Teléfono<br> +56998114750<br> (Felipe Zapata)<br> </p> <p> Dirección<br> Avenida España 1025<br> Región de los Ríos<br> Valdivia, Chile<br> </p> <p>Al encontrarse efectuada la transferencia se podrá visualizar "confirmado" en la lista de inscritos.</p> </div>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            print('Enviado :v')
            return redirect(redireccion)
    else:
        form = PersonaForm()
        print('No request')
    context = {
        'form': form,
    }
    return render(request, 'web/form-inscripcion.html', context)


"""

import random
from django.utils import timezone
from inscripcion.models import *

dd_al = random.randint(1 , 28)
mm_al = random.randint(1, 12)
aaaa_al = random.randint(1959, 2012)


pagado_al = random.choice([True, False])
rut_al = random.randint(10000000, 999999999)
nombre_al = random.choice(['Alverto', 'Beatriz', 'Claudio', 'Diana', 'Elisabeth'])
apellido_al = random.choice(['Alvarado', 'Bascuaan', 'Carcamo', 'Duarte', 'Eisch'])
sexo_al = random.choice(['Hombre', 'Mujer'])
email_al = random.choice(['Alverto@email.com', 'Beatriz@email.com', 'Claudio@email.com', 'Diana@email.com', 'Elisabeth'])
medio_pago = random.choice(CHOICES_PAGO)
telefono_al = str(random.randint(11111111, 999999999))
direcion_al = random.choice(['aaaaaaaaaaaa', 'bbbbbbbbbbbbb', 'ccccccccccccccc', 'ddddddddddddddddd'])
distancia_al = random.choice(CHOICES_DISTANCIA)
#cateogria_al = random.choice(CHOICES_CATEGORIA)
club_al = random.choice(['aaaaaaaaaaaa', 'bbbbbbbbbbbbb', 'ccccccccccccccc', 'ddddddddddddddddd'])
talla_polera_al = random.choice(CHOICES_TALLA)
medio_pago_al = random.choice(CHOICES_PAGO)"""

"""
    pagado = models.BooleanField(default=False, help_text='Marcar si se realizó la transferencia')
    rut = models.CharField('RUT', max_length=11, help_text='12345678-5')
    nombre = models.CharField('Nombre', max_length=16, help_text='Alvaro')
    apellido_pat = models.CharField('Apellido Paterno', max_length=16, help_text='Alvarado')
    apellido_mat = models.CharField('Apellido Materno', max_length=16, help_text='Aguirre')
    sexo = models.CharField(max_length=6, choices=CHOICES_SEXO, default='HOMBRE')
    email = models.EmailField()
    fecha_nacimiento = models.DateField('Fecha de Nacimiento')

    telefono = models.CharField('Teléfono', max_length=16)
    celular = models.CharField('Celular', max_length=16)
    direccion = models.CharField('Dirección', max_length=64)
    distancia = models.CharField('Distancia', max_length=3, choices=CHOICES_DISTANCIA)
    categoria = models.CharField('Categoría', max_length=5, choices=CHOICES_CATEGORIA)
    club = models.CharField('Club', max_length=32, null=True, blank=True)
    talla_polera = models.CharField('Talla de Polera', max_length=2, choices=CHOICES_TALLA)
    medio_pago = models.CharField('Medio de Pago', max_length=8, choices=CHOICES_PAGO)

"""


def listado_inscritos(request):
    listado = Persona.objects.order_by('-id')
    context = {
        'listado': listado,
    }
    return render(request, 'web/listado-inscripcion.html', context)
