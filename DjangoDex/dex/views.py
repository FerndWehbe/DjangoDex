from dex.models import Pokemon, Ability, ElementType
from django.shortcuts import render
from django.views import generic

# Create your views here.


def index(request):
    return render(request, "base_generic.html")


class PokemonListView(generic.ListView):
    model = Pokemon
    paginate_by: int = 30
    template_name: str = "pokemon_list.html"
