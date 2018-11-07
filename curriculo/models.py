from django.db import models

TIPOS = (
    ('TECNICO', 'Técnico'),
    ('GRADUACAO', 'Graduação'),
    ('PGRADUACAO', 'Pós-Graduação')
)

SEMESTRES = (
    ('PRIMEIRO', 'Primeiro Semestre'),
    ('SEGUNDO', 'Segundo Semestre'),
    ('TERCEIRO', 'Terceiro Semestre'),
    ('QUARTO', 'Quarto Semestre')
)

# Create your models here.
class Curso(models.Model):
    nome = models.CharField('Nome', max_length=120)

    sigla = models.CharField("Sigla", max_length=5, unique=True)

    tipo = models.CharField("Tipo", max_length=30, choices = TIPOS)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'CURSO'


class Disciplina(models.Model):

    nome = models.CharField("Nome", max_length=120)

    abrev = models.CharField("Abreviação", max_length=10, default='Abreviação', unique=True)

    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    descricao = models.TextField("Descrição", null=True, max_length=500)

    ementa = models.TextField("Ementa", null=True, max_length=500)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'DISCIPLINA'


class DisciplinasOfertadas(models.Model):

    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    disciplina = models.ForeignKey(Disciplina, null=True, on_delete=models.DO_NOTHING)

    semestre = models.CharField("Semestre", max_length=120, choices = SEMESTRES)

    ano = models.IntegerField("Ano", null=True)
    
    class Meta:
        db_table = 'DISCIPLINAOFERTADA'
        verbose_name = 'Disciplina Ofertada'
        verbose_name_plural = 'Disciplinas Ofertadas'