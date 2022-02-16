from django.contrib import admin
from .models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'come_cat')
    list_display_links = ('id', 'come_cat')


admin.site.register(Categoria, CategoriaAdmin)