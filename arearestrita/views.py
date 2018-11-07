from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def testa_professor(usuario):
    return usuario.tipo == 'P'

def testa_aluno(usuario):
    return usuario.tipo == 'A'

def testa_coordenador(usuario):
    return usuario.tipo == 'C'


@login_required
@user_passes_test(testa_professor)
def home_professor(request):
    return render(request, 'arearestrita/home.html')

@login_required
@user_passes_test(testa_aluno)
def home_aluno(request):
    return render(request, 'arearestrita/home.html')

@login_required
@user_passes_test(testa_coordenador)
def home_coordenador(request):
    return render(request, 'arearestrita/home.html')