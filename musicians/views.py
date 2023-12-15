from django.shortcuts import get_object_or_404, redirect, render

from musicians.form.album import AlbumForm
from musicians.form.musician import MusicianForm
from musicians.models.album import Album
from musicians.models.musician import Musician


def index(args):
    return redirect("/musicians")


def add_musician(request):
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("musician_list")
    else:
        form = MusicianForm()
    return render(request, "add_musician.html", {"form": form})


def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, "musician_list.html", {"musicians": musicians})


def edit_musician(request, musician_id):
    musician = get_object_or_404(Musician, pk=musician_id)
    if request.method == "POST":
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect("musician_list")
    else:
        form = MusicianForm(instance=musician)
    return render(request, "edit_musician.html", {"form": form, "musician": musician})


def delete_musician(request, musician_id):
    musician = get_object_or_404(Musician, pk=musician_id)
    musician.delete()
    return redirect("musician_list")


def add_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("album_list")
    else:
        form = AlbumForm()
    return render(request, "add_album.html", {"form": form})


def album_list(request):
    albums = Album.objects.all()
    return render(request, "album_list.html", {"albums": albums})


def edit_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("album_list")
    else:
        form = AlbumForm(instance=album)
    return render(request, "edit_album.html", {"form": form, "album": album})


def delete_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    album.delete()
    return redirect("album_list")
