from django.contrib import admin
from app_cad_usuarios.models import Usuario

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade')

admin.site.register(Usuario, UsuariosAdmin)
