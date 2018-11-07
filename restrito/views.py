from django.shortcuts import render

# Create your views here.

def aluno(request):
    context = {
        "titulo":"Área do Aluno",
    }
    return render(request, "aluno.html", context)

def professor(request):
    context = {
        "titulo":"Área do Professor",
    }
    return render(request, "professor.html", context)

def turma(request):
    context = {
        "titulo":"Turma",
    }
    return render(request, "turma.html", context)

def atividade(request):
    context = {
        "titulo":"Atividades",
    }
    return render(request, "atividade.html", context)
