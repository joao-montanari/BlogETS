from django import views
from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('', views.home_index, name='homeindex'),
    path('postagem/', views.home_postagem, name='homepostagem'),
    path('missao/', views.home_missao, name='homemissao'),
    path('detalhes/<int:id>', views.home_detalhes, name='homedetalhes'),
    path('postcursos/', views.home_postcursos, name='homepostcursos'),
]
