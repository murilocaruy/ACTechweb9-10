from django.urls import path

from curriculo import views

app_name = "curriculo"
urlpatterns = [
    path('novo/', views.novo_curso, name='novo_curso'),
    path('<str:sigla>/', views.curso, name="curso"),
    path('<str:sigla>/disciplina/<str:abrev>/', views.disciplina, name="disciplina"),
]