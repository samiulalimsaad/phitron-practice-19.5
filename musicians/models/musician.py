from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(max_length=50)
    albums = models.ManyToManyField("album")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
