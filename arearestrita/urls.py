from django.urls import path
from .views import home_professor, home_aluno
from arearestrita import views

app_name = 'arearestrita'
urlpatterns = [
    path('professor', home_professor, name="home_professor"),
    path('aluno', home_aluno, name="home_aluno"),
    path('professor/novaatividade', views.nova_atividade, name="novaatividade"),
    path('professor/vincularatividade', views.vincular_atividade, name="vincularatividade")
]
