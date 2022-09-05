from gc import get_objects
from django.shortcuts import get_object_or_404, redirect, render

from home.models import Postagem

# Create your views here.
def home_index(request):
    return render(request, 'home/index.html')

def home_postagem(request):
    return render(request, 'home/postagem.html')

def home_missao(request):
    return render(request, 'home/missao.html')

def home_detalhes(request, id):
    context = get_object_or_404(
        Postagem, id=id
    )
    return render(request, 'home/detalhes.html', {'postagens' : context})

def home_postcursos(request):
    dados_sql = Postagem.objects.all()
    context = {
        'Postagens' : dados_sql
    }

    return render(request, 'home/postcursos.html', context)