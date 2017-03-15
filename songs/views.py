from django.shortcuts import render, get_object_or_404

from django.http import Http404

from .models import Song, Performer


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs/song_list.html', {'songs': songs})


def song_detail(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        raise Http404()
    else:
        return render(request, 'songs/song_list.html', {'song': song})


def performer_detail(request, pk):
    try:
        performer = Performer.objects.get(pk=pk)
    except Performer.DoesNotExist:
        raise Http404()
    else:
        return render(request, 'songs/performer_detail.html', {'performer': performer})
