from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView



# Create your views here.
# def homepage(request):
#     return render(request, 'homepage.html')

class Homepage(TemplateView):
    template_name = 'homepage.html'


# nova pagina = URL + View + Html
# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, 'homefilmes.html', context)

class Homefilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme
    #object_list -> lista de itens do modelo


class Detalhesfilme(DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme
    # object -> 1 item do nosso modelo