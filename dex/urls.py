from django.urls import path
from dex import views

urlpatterns = [
    path("", views.index, name="dex"),
    path("pokemon_search/", views.pokemon_search, name="pokemon_search"),
    path("move_search/", views.move_search, name="move_search"),
    path("type_search/", views.type_search, name="type_search"),
    path("ability_search/", views.ability_search, name="ability_search"),
]


# Class View
urlpatterns += [
    path("pokes/", views.PokemonListView.as_view(), name="pokes"),
    path(
        "pokes/<slug:slug>",
        views.PokemonDetailView.as_view(),
        name="pokemon-detail",
    ),
    path("moves/", views.MoveListView.as_view(), name="moves"),
    path(
        "moves/<slug:slug>", views.MoveDetailView.as_view(), name="move-detail"
    ),
    path(
        "element_types/",
        views.ElementTypeListView.as_view(),
        name="element_types",
    ),
    path(
        "element_types/<slug:slug>",
        views.ElementTypeDetailView.as_view(),
        name="element_type-detail",
    ),
    path(
        "abilities/",
        views.AbilityListView.as_view(),
        name="abilities",
    ),
    path(
        "abilities/<slug:slug>",
        views.AbilityDetailView.as_view(),
        name="ability-detail",
    ),
]


# API

urlpatterns += [
    path("list_all_pokes/", views.list_all_pokes, name="list_all_pokes")
]
