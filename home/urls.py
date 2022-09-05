from django import views
from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('', views.home_index, name='homeindex'),
    path('postagem/', views.home_postagem, name='homepostagem'),
    path('missao/', views.home_missao, name='homemissao'),
    path('post/<int:id>', views.home_post, name='homepost'),
    path('posts/', views.home_posts, name='homeposts'),
]
