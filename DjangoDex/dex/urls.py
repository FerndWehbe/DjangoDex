from django.urls import path
from dex import views

urlpatterns = [
    path("", views.index, name="dex"),
    path("pokemon_search/", views.pokemon_search, name="pokemon_search"),
    path("move_search/", views.move_search, name="move_search"),
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
]


# API

urlpatterns += [
    path("list_all_pokes/", views.list_all_pokes, name="list_all_pokes")
]
