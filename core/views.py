from django.shortcuts import render, redirect

from .forms import ContatoForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

# Create your views here.
def home(request):
    context = {
        "titulo":"Outro Título",
    }
    return render(request, "index.html", context)

def contato(request):
    context = {}

    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            context["mensagem"] = "Mensagem enviada com sucesso"
        else:
            context["mensagem"] = "Problemas ao enviar a mensagem"
    else:
        form = ContatoForm()

    context["form"] = form
    return render(request, "contato.html", context)

def entrar(request):
    context = {}

    if request.POST:
        username = request.POST.get('login')
        senha = request.POST.get('senha')

        usuario = authenticate(username=username, password=senha)
    
        if usuario:
            login(request, usuario)
            if usuario.tipo == 'P':
                return redirect('arearestrita:home_professor')
            elif usuario.tipo == 'A':
                return redirect('arearestrita:home_aluno')
            else:
                return redirect('admin:index')
            
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return render(request, "login.html", context)

def sair(request):
    logout(request)
    return redirect('core:home')