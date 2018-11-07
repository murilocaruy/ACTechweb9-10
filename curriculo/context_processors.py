from curriculo.models import Curso, DisciplinasOfertadas, Disciplina

def lista_cursos(request):
    return {
        "curso": Curso.objects.all()
    }

def lista_disciplinasOfertadas(request):
    return {
        "disciplinasOfertadas": DisciplinasOfertadas.objects.all()
    }

def lista_disciplinas(request):
    return{
        "disciplinas": Disciplina.objects.all()
    }