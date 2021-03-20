from django.contrib import admin
from .models import RazaModel, EspecieModel, ClienteModel, PromocionModel, MascotaModel


# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/
class RazaAdmin(admin.ModelAdmin):
    # para modificar la vista del modelo:
    list_display = ('razaNombre', 'especie')
    # para agregar un buscador del modelo:
    # si queremos hacer una busqueda de una FK tenemos que especificar a que columna vamos a hacer la busqueda del padre mediante doble subguion y luego indicar la columna o atributo
    search_fields = ('razaNombre', 'especie__especieNombre')
    # si queremos ver un filtro generico (se recomienda solamente usar las columnas que no se repitan los datos)
    list_filter = ('especie',)
    # si queremos ver los campos de solamente lectura (no se pueden escribir)
    readonly_fields = ('razaId',)
    ordering = ('razaNombre',)


class PromocionAdmin(admin.ModelAdmin):
    list_display = ['promocionDescripcion', 'promocionEstado']
    list_filter = ['promocionEstado']


class EspecieAdmin(admin.ModelAdmin):
    list_display = ['especieNombre']


admin.site.register(RazaModel, RazaAdmin)
admin.site.register(EspecieModel, EspecieAdmin)
admin.site.register(ClienteModel)
admin.site.register(PromocionModel, PromocionAdmin)
admin.site.register(MascotaModel)
