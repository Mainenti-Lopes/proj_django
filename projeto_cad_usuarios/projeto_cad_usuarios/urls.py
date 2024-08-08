
from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # rota, view responsável, nome de referência
    path('', views.home, name='home'),
    # usuarios.com/usuarios
    path('novo_usuario/', views.novo_usuario, name='novo_usuario'),
    path('usuarios/', views.mostra_usuarios, name='mostra_usuarios'),
    path('usuarios/confirm_remove/<int:id_entrada>', views.confirm_remove, name='confirm_remove'),
    path('usuarios/remove_usuario/<int:id_entrada>', views.remove_usuario, name='remove_usuario'),
    # testando
    path('teste/<name>/<int:age>/', views.teste, name='teste')
]
