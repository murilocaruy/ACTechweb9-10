from django.contrib import admin
from curriculo.models import Curso, Disciplina, DisciplinasOfertadas

# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'tipo')
    list_filter = ('tipo',)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'abrev', 'curso')
    list_filter = ('curso',)

class DisciplinasOfertadasAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'curso', 'semestre', 'ano')
    list_filter = ('disciplina', 'curso', 'semestre', 'ano')

admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(DisciplinasOfertadas, DisciplinasOfertadasAdmin)