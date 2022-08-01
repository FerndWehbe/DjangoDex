from typing import Any, Dict
from django.db.models import Model
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from dex.models import Pokemon, Ability, ElementType, Move, MoveByLevel
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import generic

# Create your views here.


def index(request):
    # return render(request, "base_generic.html")
    # return render(request, "base.html")
    return redirect("pokes")


def pokemon_search(request):
    q = request.GET.get("pokemon_name")
    if q is None:
        messages.info(request, "Pokemon não encontrado!")
        return HttpResponseRedirect("/pokes")
    try:
        pokemon = Pokemon.objects.filter(name__icontains=q).first()
        if not pokemon:
            messages.info(request, "Pokemon não encontrado!")
            return HttpResponseRedirect("/pokes")
        return redirect(f"/pokes/{pokemon}")
    except Exception:
        messages.info(request, "Pokemon não encontrado!")
        return HttpResponseRedirect("/pokes")


def move_search(request):
    q = request.GET.get("move_name")
    if q is None:
        messages.info(request, "Move não encontrado!")
        return HttpResponseRedirect("/moves")
    try:
        move = Move.objects.filter(move_name__icontains=q).first()
        if not move:
            messages.info(request, "Move não encontrado!")
            return HttpResponseRedirect("/moves")
        return redirect(f"/moves/{move.move_name.lower()}")
    except Exception:
        messages.info(request, "Move não encontrado!")
        return HttpResponseRedirect("/moves")


def type_search(request):
    q = request.GET.get("type_name")
    if q is None:
        messages.info(request, "Type não encontrado!")
        return HttpResponseRedirect("/element_types")
    try:
        element_type = ElementType.objects.filter(name__icontains=q).first()
        if not element_type:
            messages.info(request, "Type não encontrado!")
            return HttpResponseRedirect("/element_types")
        return redirect(f"/element_types/{element_type.name.lower()}")
    except Exception:
        messages.info(request, "Type não encontrado!")
        return HttpResponseRedirect("/element_types")


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
        context["pokemons"] = Pokemon.objects.filter(
            move_by_level__learned_move=kwargs["object"]
        )
        return context


class ElementTypeListView(generic.ListView):
    model: Model = ElementType
    template_name: str = "element_type_list.html"


class ElementTypeDetailView(generic.DetailView):
    model: Model = ElementType
    template_name: str = "element_type_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["pokemons"] = Pokemon.objects.filter(
            types__name=kwargs["object"]
        )
        return context


# API
def list_all_pokes(request):
    poke = Pokemon.objects.values_list("name")
    result = [name[0] for name in poke]
    return JsonResponse(result, safe=False)
