from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from musicians.form.album import AlbumForm
from musicians.form.musician import MusicianForm
from musicians.form.registration import RegistrationForm
from musicians.models.album import Album
from musicians.models.musician import Musician


def index(args):
    return redirect("/musicians")


@login_required(login_url="/login/")
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


@login_required(login_url="/login/")
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


@login_required(login_url="/login/")
def delete_musician(request, musician_id):
    musician = get_object_or_404(Musician, pk=musician_id)
    musician.delete()
    return redirect("musician_list")


@login_required(login_url="/login/")
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


@login_required(login_url="/login/")
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


@login_required(login_url="/login/")
def delete_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    album.delete()
    return redirect("album_list")


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Logged In Successfully")
                return redirect("index")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def user_logout(request):
    username = request.user.username
    logout(request)
    messages.warning(request, f"Logged Out Successfully")
    return redirect("index")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"Your account has been created successfully. Please log in.",
            )
            return redirect("login")
    else:
        form = RegistrationForm()

    return render(request, "signup.html", {"form": form})
