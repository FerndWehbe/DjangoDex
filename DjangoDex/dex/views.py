from typing import Any, Dict
from django.db.models import Model
from dex.models import Pokemon, Ability, ElementType, Move, MoveByLevel
from django.shortcuts import redirect, render
from django.views import generic

# Create your views here.


def index(request):
    # return render(request, "base_generic.html")
    # return render(request, "base.html")
    return redirect("pokes")


class PokemonListView(generic.ListView):
    model: Model = Pokemon
    paginate_by: int = 30
    template_name: str = "pokemon_list.html"


class PokemonDetailView(generic.DetailView):
    model: Model = Pokemon
    template_name: str = "pokemon_detail.html"


class MoveListView(generic.ListView):
    model: Model = Move
    paginate_by: int = 32
    template_name: str = "move_list.html"


class MoveDetailView(generic.DetailView):
    model: Model = Move
    template_name: str = "move_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        moves = Pokemon.objects.filter(
            move_by_level__learned_move=kwargs["object"]
        )
        context["pokemons"] = moves
        return context
