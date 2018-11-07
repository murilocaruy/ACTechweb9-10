"""arearestrita URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from restrito import views

app_name = 'restrito'
urlpatterns = [
    path('aluno/', views.aluno, name="aluno"),
    path('professor/', views.professor, name="professor"),
    path('perfil/turma/idturma/', views.turma, name="turma"),
    path('perfil/turma/idturma/atividade/idatividade/', views.atividade, name="atividade"),
]
