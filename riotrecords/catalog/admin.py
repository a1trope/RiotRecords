from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ["album_name", "band_name", "price", "year"]


admin.site.register(Item, ItemAdmin)
