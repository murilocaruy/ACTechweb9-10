from django.shortcuts import render, get_object_or_404
from curriculo.models import Curso, Disciplina
from curriculo.forms import CursoForm

def curso(request, sigla):
    curso = get_object_or_404(Curso, sigla=sigla)
    context = {
        "atual": curso
    }
    return render(request, "curriculo/curso.html", context)

def disciplina(request, sigla, abrev):
    disciplinas = get_object_or_404(Disciplina, abrev=abrev)
    context = {
        "detalhes": disciplinas
    }
    return render(request, "curriculo/disciplina.html", context)

def novo_curso(request):
    context = {}

    if request.POST:
        pass
    else:
        form =  CursoForm()
    context["form"] = form
    
    return render(request, "curriculo/novo_curso.html")
