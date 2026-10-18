from django.contrib import admin
from .models import DJ


@admin.register(DJ)
class DJAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estilo', 'nacionalidad', 'debut_year')
    search_fields = ('nombre', 'nacionalidad')     # búsqueda en la caja del admin
    list_filter = ('estilo', 'nacionalidad')       # filtros laterales 