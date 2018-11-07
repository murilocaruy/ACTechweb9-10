from django.db import models
from restrito.models import Professor, Aluno
from curriculo.models import DisciplinasOfertadas
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

STATUS = (
    ('D', 'Disponibilizada'),
    ('A', 'Aberta'),
    ('F', 'Fechada'),
    ('E', 'Encerrada'),
    ('P', 'Prorrogada')
)

TIPOS = (
    ('ABERTA', 'Resposta Aberta'),
    ('TESTE', 'Teste')
)

STATUSATIV = (
    ('E', 'Entregue'),
    ('C', 'Corrigido')
)

STATUSMSG = (
    ('E', 'Enviado'),
    ('L', 'Lido'),
    ('R', 'Respondido')
)


class Atividade(models.Model):
    titulo = models.CharField('Título', max_length=120, unique=True)

    descricao = models.TextField('Descrição', max_length=800)

    conteudo = models.TextField('Conteúdo', max_length=500)

    tipo = models.CharField('Tipo', max_length=30, choices = TIPOS)

    extras = models.TextField('Conteúdo', max_length=300)

    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'ATIVIDADE'


class AtividadeVinculada(models.Model):
    
    atividade = models.ForeignKey(Atividade, on_delete=models.DO_NOTHING)

    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)

    disciplina_ofertada = models.ForeignKey(DisciplinasOfertadas, on_delete=models.DO_NOTHING)

    rotulo = models.CharField('Rótulo', max_length=120, unique=True)

    status = models.CharField('Status', max_length=30, choices = STATUS)

    DtInicioRespostas = models.DateTimeField('Data de Início')

    DtFimRespostas = models.DateTimeField('Data Limite')

    class Meta:
        db_table = 'ATIVIDADEVINCULADA'


class Entrega(models.Model):

    aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING)

    atividade_vinculada = models.ForeignKey(AtividadeVinculada, on_delete=models.DO_NOTHING)

    titulo = models.CharField('Título', max_length=120)

    resposta = models.TextField('Resposta', max_length=600)

    dtentrega = models.DateTimeField('Data de Entrega')

    status = models.CharField('Status', max_length=30, choices = STATUSATIV, default='E')

    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)

    nota = models.IntegerField('Nota', validators=[MaxValueValidator(10), MinValueValidator(1)])

    dtavaliacao = models.DateTimeField('Data de Avaliação')

    obs = models.TextField('Observações', max_length=300)

    class Meta:
        db_table = 'ENTREGA'


class Mensagem(models.Model):

    aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING)

    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)

    assunto = models.CharField('Assunto', max_length=120)

    referencia = models.CharField('Referência', max_length=120)

    conteudo = models.TextField('Conteúdo', max_length=600)

    status = models.CharField('Status', max_length=30, choices = STATUSMSG)

    dtenvio = models.DateTimeField('Data de Envio')

    dtresposta = models.DateTimeField('Data de Resposta')

    resposta = models.TextField('Resposta', max_length=600)

    class Meta:
        db_table = 'MENSAGEM'



