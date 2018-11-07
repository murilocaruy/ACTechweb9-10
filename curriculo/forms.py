from django import forms
from curriculo.models import Curso

class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ['nome', 'sigla', 'tipo']