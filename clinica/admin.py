from django.contrib import admin
from .models import Especialidades,Agenda,Cliente,Consulta
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('nome')
    list_display_links = ('nome')
    search_fields = ('nome',)
    list_per_page = 10
    ordering = ('nome',)

admin.site.register(Especialidades)
class AgendaAdmin(admin.ModelAdmin):
    list_display=('medico')
    list_display_links=('medico')
    search_fields=('dia')
    list_per_page=(10)
    ordering=('dia')
admin.site.register(Agenda)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('first_name')
    list_display_links=('first_name')
    list_per_page=(10)
    ordering=('user')
admin.site.register(Cliente)
class ConsultaAdmin(admin.ModelAdmin):
    list_display=('data')
    list_display_links=('medico')
    list_per_page=(10)
    ordering=('data')
admin.site.register(Consulta)