from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Professor, Usuario, Aluno

# Register your models here.

class UsuarioCriacaoForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('username',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password('123@mudar')
        if commit:
            user.save()
        return user

class UsuarioAlteracaoForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'data_expiracao')

class ProfessorInline(admin.StackedInline):
    model = Professor
    max_num = 1

class AlunoInline(admin.StackedInline):
    model = Aluno
    max_num = 1

class UsuarioAdmin(UserAdmin):
    form = UsuarioAlteracaoForm
    add_form = UsuarioCriacaoForm
    inlines = (ProfessorInline,)
    list_filter = ()
    list_display = ('username', 'tipo')
    fieldsets = (
        (None, {'fields': ('username', 'data_expiracao')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username',)}),
    )

    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

    def save_model(self, request, obj, form, change):
        obj.tipo = 'P'
        super(UsuarioAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        resultado = super(UsuarioAdmin, self).get_queryset(request)
        return resultado.filter(tipo='P')

class AlunoUsuarioAdmin(UserAdmin):
    form = UsuarioAlteracaoForm
    add_form = UsuarioCriacaoForm
    inlines = (AlunoInline,)
    list_filter = ()
    list_display = ('username', 'tipo')
    fieldsets = (
        (None, {'fields': ('username', 'data_expiracao')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username',)}),
    )

    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

    def save_model(self, request, obj, form, change):
        obj.tipo = 'A'
        super(AlunoUsuarioAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        resultado = super(AlunoUsuarioAdmin, self).get_queryset(request)
        return resultado.filter(tipo='A')


class ProfessorUsuario(Usuario):
    class Meta:
        proxy = True
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

admin.site.register(ProfessorUsuario, UsuarioAdmin)

class AlunoUsuario(Usuario):
    class Meta:
        proxy = True
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

admin.site.register(AlunoUsuario, AlunoUsuarioAdmin)