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

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacao += 1
        filme.save()
        return super().get(request, *args, **kwargs) #redireciona o usuário para o URL final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # filtrar a minha tabela de filmes pegando os filmes cuja categoria é igual a categoria do filme da pagina (object)
        # self.get_object()
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)
        context['filmes_relacionados'] = filmes_relacionados
        return context


class Pesquisafilme(ListView):
    template_name = 'pesquisa.html'
    model = Filme

    #object_list
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None