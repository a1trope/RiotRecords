from django.db import models
from catalog.models import Item
from django.contrib.auth.models import User


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CartItem(id={self.id}, user={self.user}, item={self.item})"
