# music_lyrics/views.py
from django.shortcuts import render, get_object_or_404
from .models import Lyrics
from .forms import LyricsForm
from django.http import HttpResponseRedirect



def lyrics_list(request):
    lyrics = Lyrics.objects.all()
    return render(request, 'music_lyrics/lyrics_list.html', {'lyrics': lyrics})

def lyrics_detail(request, pk):
    lyric = get_object_or_404(Lyrics, pk=pk)
    return render(request, 'music_lyrics/lyrics_detail.html', {'lyric': lyric})

def lyrics_create(request):
    form = LyricsForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/lyrics/')  # Redirect to the lyrics list
    return render(request, 'music_lyrics/lyrics_form.html', {'form': form})

def lyrics_update(request, pk):
    lyric = get_object_or_404(Lyrics, pk=pk)
    form = LyricsForm(request.POST or None, instance=lyric)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('/lyrics/')  # Redirect to the lyrics list
    return render(request, 'music_lyrics/lyrics_form.html', {'form': form})

def lyrics_delete(request, pk):
    lyric = get_object_or_404(Lyrics, pk=pk)
    lyric.delete()
    return HttpResponseRedirect('/lyrics/')  # Redirect back to the lyrics list
