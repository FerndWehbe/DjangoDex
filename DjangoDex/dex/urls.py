from django.urls import path
from dex import views

urlpatterns = [
    path("", views.index, name="dex"),
]


urlpatterns += [
    path("pokes/", views.PokemonListView.as_view(), name="pokes"),
]
