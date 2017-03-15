from django.shortcuts import render, get_list_or_404

from django.http import Http404

from .models import Song, Performer


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs/song_list.html', {'songs': songs})

def