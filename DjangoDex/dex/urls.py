from django.urls import path
from dex import views

urlpatterns = [
    path("", views.index, name="dex"),
]


# Class View
urlpatterns += [
    path("pokes/", views.PokemonListView.as_view(), name="pokes"),
    path(
        "pokes/<slug:slug>",
        views.PokemonDetailView.as_view(),
        name="pokemon-detail",
    ),
]