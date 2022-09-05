from ast import AugStore
from sqlite3 import Cursor
from django.db import models

# Create your models here.
class Postagem(models.Model):
    curso = models.CharField(max_length = 50)
    titulo = models.CharField(max_length = 50)
    sub_titulo = models.CharField(max_length = 50)
    autor = models.CharField(max_length = 50)
    conteudo = models.TextField(max_length = 1000)

class Respostas(models.Model):
    autor = models.CharField(max_length = 50)
    resposta = models.TextField(max_length = 1000)
    postagem = models.ForeignKey(Postagem, on_delete = models.PROTECT)