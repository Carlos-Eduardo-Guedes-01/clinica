from django.contrib import admin
from .models import Especialidades
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('nome')
    list_display_links = ('nome')
    search_fields = ('nome',)
    list_per_page = 10
    ordering = ('nome',)

admin.site.register(Especialidades)