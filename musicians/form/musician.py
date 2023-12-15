from django import forms

from musicians.models.album import Album
from musicians.models.musician import Musician


class MusicianForm(forms.ModelForm):
    albums = forms.ModelMultipleChoiceField(
        queryset=Album.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Musician
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "instrument_type",
            "albums",
        ]
