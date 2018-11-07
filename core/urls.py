from django.urls import path

from core import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name="home" ),
    path('contact/', views.contato, name="contato"),
    path('entrar/', views.entrar, name="entrar"),
    path('sair/', views.sair, name="sair")
]