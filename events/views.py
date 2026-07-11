from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .models import Event, Registration
from .forms import EventForm


def home(request):

    eventi = Event.objects.all()

    return render(
        request,
        "events/home.html",
        {"eventi": eventi}
    )


def nuovo_evento(request):

    if request.method == "POST":

        form = EventForm(request.POST)

        if form.is_valid():

            evento = form.save(commit=False)

            if request.user.is_authenticated:
                evento.organizer = request.user

            evento.save()

            return redirect("/")

    else:

        form = EventForm()

    return render(
        request,
        "events/nuovo_evento.html",
        {"form": form}
    )


def dettaglio_evento(request, event_id):

    evento = Event.objects.get(id=event_id)

    partecipanti = Registration.objects.filter(
        event=evento
    )

    return render(
        request,
        "events/dettaglio_evento.html",
        {
            "evento": evento,
            "partecipanti": partecipanti
        }
    )


def modifica_evento(request, event_id):

    evento = Event.objects.get(id=event_id)

    if request.method == "POST":

        form = EventForm(
            request.POST,
            instance=evento
        )

        if form.is_valid():

            form.save()

            return redirect("/")

    else:

        form = EventForm(instance=evento)

    return render(
        request,
        "events/modifica_evento.html",
        {
            "form": form,
            "evento": evento
        }
    )


def elimina_evento(request, event_id):

    evento = Event.objects.get(id=event_id)

    evento.delete()

    return redirect("/")


@login_required
def registrazione_evento(request, event_id):

    evento = Event.objects.get(id=event_id)

    Registration.objects.get_or_create(
        user=request.user,
        event=evento
    )

    return redirect("/")
class EventListView(ListView):

    model = Event

    template_name = "events/home.html"

    context_object_name = "eventi"