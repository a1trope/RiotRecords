from django.db import models


class Item(models.Model):
    album_name = models.CharField(max_length=150)
    band_name = models.CharField(max_length=150)
    price = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.album_name} - {self.band_name}"

