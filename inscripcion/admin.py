# coding=utf-8
from django.contrib import admin
import xlwt

# Register your models here.
from .models import Persona, CategoriaACompetir
from django.http import HttpResponse


def export_xls(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Listado-Inscritos.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Inscripciones")

    row_num = 0

    columns = [
        # aquí los campos escritos en el Documento..
        (u"ID", 1999),
        (u"PAGADO", 2000),
        (u"RUT", 2001),
        (u"NOMBRE", 2002),
        (u"APELLIDO PATERNO", 2003),
        (u"APELLIDO MATERNO", 2004),
        (u"GENERO", 2005),
        (u"EMAIL", 2006),
        (u"FECHA DE NACIMIENTO", 2007),
        (u"EDAD", 2017),
        (u"TELEFONO", 2008),
        (u"CELULAR", 2009),
        (u"COMUNA", 2010),
        (u"NACIONALIDAD", 2011),
        (u"DIRECCIÓN", 2012),
        (u"CLUB", 2013),
        (u"TALLA POLERA", 2014),
        (u"MEDIO PAGO", 2015),
        (u"CATEGORÍA A COMPETIR", 2016),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for obj in Persona.objects.get_queryset():
        row_num += 1
        row = [
            # aquí los campos a exportar en excel
            obj.id,
            obj.estado(),
            obj.rut,
            obj.nombre,
            obj.apellido_pat,
            obj.apellido_mat,
            obj.sexo,
            obj.email,
            obj.fecha_nacimiento.isoformat(),
            obj.edad(),
            obj.telefono,
            obj.celular,
            obj.comuna,
            obj.nacionalidad,
            obj.direccion,
            obj.club,
            obj.talla_polera,
            obj.medio_pago,
            obj.edad_y_precio.__unicode__(),
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


export_xls.short_description = u"Exportar XLS"


class CategoriaACompetirAdmin(admin.ModelAdmin):
    list_filter = ['nombre_categoria', 'edad', 'precio']


admin.site.register(CategoriaACompetir, CategoriaACompetirAdmin)


class PersonaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'rut', 'apellido_pat', 'nombre']
    list_filter = ['anno', 'pagado', 'club', ]
    list_display = ['id', 'rut', 'apellido_pat', 'nombre', 'edad_y_precio']
    fieldsets = (
        ('Pagos', {
            'fields': ('anno','medio_pago', 'edad_y_precio', 'pagado')
        }),
        ('Personales', {
            'fields': (
                ('rut'), 'nombre', ('apellido_pat', 'apellido_mat'), 'sexo', 'fecha_nacimiento')
        }),
        ('Contacto', {
            'fields': (
                ('telefono', 'celular'), ('comuna', 'direccion'), 'nacionalidad', 'club', 'talla_polera')
        })
    )
    list_display_links = ['id', 'rut', 'apellido_pat', 'nombre', 'edad_y_precio']
    actions = [export_xls]

    class Meta:
        model = Persona


admin.site.register(Persona, PersonaAdmin)
