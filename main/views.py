from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, MovieSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Create your views here.

def wszystkie_filmy(request):

    # text_views = 'to jest text z views'
    filmy = Movie.objects.all()
    # return render(request, 'lista_filmow.html',
    #               {'text': text_views, 'filmy': filmy, 'moze_ogladac': True})
    return render(request, 'lista_filmow.html', {'filmy': filmy})


@login_required
def nowy_film(request):

    form = MovieForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form})


@login_required
def edytuj_film(request, id):

    film = get_object_or_404(Movie, pk = id)    #pk - primary key
    form = MovieForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form})


@login_required
def usun_film(request, id):

    film = get_object_or_404(Movie, pk = id)

    if request.method == 'POST':
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html', {'film':film})

