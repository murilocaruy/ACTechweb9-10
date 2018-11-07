from django.urls import path
from .views import home_professor, home_aluno

app_name = 'arearestrita'
urlpatterns = [
    path('professor', home_professor, name="home_professor"),
    path('aluno', home_aluno, name="home_aluno"),
]