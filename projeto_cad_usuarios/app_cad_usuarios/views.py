from django.shortcuts import render, HttpResponse
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def novo_usuario(request):
    # Salvar os dados da tela para o banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    return render(request, 'usuarios/novo_usuario.html')

def mostra_usuarios(request):
    # Exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)

def confirm_remove(request, id_entrada):
    obj_usuario = Usuario.objects.get(id_usuario=id_entrada)
    usuario = {"id_usuario": obj_usuario.id_usuario, "nome": obj_usuario.nome, "idade": obj_usuario.idade}
    return render(request, 'usuarios/confirm_remove.html', usuario)

def remove_usuario(request, id_entrada):
    Usuario.objects.filter(id_usuario=id_entrada).delete()
    return render(request, 'usuarios/remove_usuario.html')

def teste(request, name, age):
    return HttpResponse('<h1>Hello {} de {} anos!</h1>' .format(name, age))