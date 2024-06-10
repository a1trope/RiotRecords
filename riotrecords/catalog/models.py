from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    album_name = models.CharField(max_length=150)
    band_name = models.CharField(max_length=150)
    price = models.IntegerField()
    year = models.IntegerField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.album_name} - {self.band_name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=[
        ("PD", "pending"),
        ("PR", "processing"),
        ("SH", "shipped"),
        ("DE", "delivered"),
    ])
    address = models.CharField(max_length=200)
    time = models.DateTimeField()

    def __str__(self):
        return f"order {self.id} (user={self.user})"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="+")
