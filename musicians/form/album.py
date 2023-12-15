from django import forms

from musicians.models.album import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["album_name", "musicians", "release_date", "rating"]
