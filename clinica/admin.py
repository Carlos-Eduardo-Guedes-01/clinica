from django.contrib import admin
from .models import Especialidades,Agenda
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