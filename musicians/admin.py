from django.contrib import admin

from musicians.models.album import Album
from musicians.models.musician import Musician

admin.site.register(
    Musician,
)
admin.site.register(
    Album,
)
