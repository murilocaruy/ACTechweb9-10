from django.contrib import admin
from django import forms
from arearestrita.models import Atividade, AtividadeVinculada, Entrega, Mensagem

# Register your models here.

admin.site.register(Atividade)
admin.site.register(AtividadeVinculada)
admin.site.register(Entrega)
admin.site.register(Mensagem)
