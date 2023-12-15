from django import forms

from musicians.models.musician import Musician


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ["first_name", "last_name", "email", "phone_number", "instrument_type"]
