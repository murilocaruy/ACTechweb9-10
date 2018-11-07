from django.db import models

class Professor(models.Model):

    nome = models.CharField("Nome Completo", max_length=120)
    email = models.EmailField("Email")
    celular = models.CharField("Celular", max_length=15)
    apelido = models.CharField("Apelido", max_length=120)
    usuario = models.ForeignKey('restrito.Usuario', on_delete=models.CASCADE)

    class Meta:
        db_table = 'PROFESSOR'
