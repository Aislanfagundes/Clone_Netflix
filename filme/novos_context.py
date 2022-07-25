from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')
    return {'lista_filmes_recentes': lista_filmes}

def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacao')
    return {'lista_filmes_emalta': lista_filmes} # é essa variação que vamos usar no HTML, então não pode ser um nome já usado

def filme_destaque(request):
    filme = Filme.objects.order_by('-data_criacao')[0]
    return {"filme_destaque": filme}