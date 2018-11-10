from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from arearestrita.forms import AtividadeForm, AtividadeVinculadaForm
from arearestrita.models import Atividade

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

'''
def nova_atividade(request):
    context = {}

    form = AtividadeForm(request.POST)
    
    context['form'] = form

    return render(request, 'arearestrita/novaatividade.html', context)
'''
'''
def nova_atividade(request):
    context = {}

    form = AtividadeForm(request.POST)

    if form.is_valid():
        titulo = form.changed_data['titulo']
        descricao = form.changed_data['descricao']
        conteudo = form.changed_data['conteudo']
        tipo = form.changed_data['tipo']
        extras = form.changed_data['extras']
        form = AtividadeForm()
        return redirect('arearestrita/home')

    context["form"] = form

    return render(request, 'arearestrita/novaatividade.html', context)    
'''

def nova_atividade(request):
    context = {}

    form = AtividadeForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('arearestrita/home')

    context["form"] = form

    return render(request, 'arearestrita/novaatividade.html', context)    

def vincular_atividade(request):
    context = {}

    form = AtividadeVinculadaForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('arearestrita/home')

    context["form"] = form

    return render(request, 'arearestrita/vincularatividade.html', context)    


