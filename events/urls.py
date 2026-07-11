from django.urls import path
from .views import *

urlpatterns = [

    path(
        "",
        EventListView.as_view(),
        name="home"
    ),

    path(
        "nuovo/",
        nuovo_evento,
        name="nuovo_evento"
    ),

    path(
        "dettaglio/<int:event_id>/",
        dettaglio_evento,
        name="dettaglio_evento"
    ),

    path(
        "modifica/<int:event_id>/",
        modifica_evento,
        name="modifica_evento"
    ),

    path(
        "elimina/<int:event_id>/",
        elimina_evento,
        name="elimina_evento"
    ),

    path(
        "registrazione/<int:event_id>/",
        registrazione_evento,
        name="registrazione_evento"
    ),
]