from django.contrib import admin
from .models import Item, Order, OrderItem


class ItemAdmin(admin.ModelAdmin):
    list_display = ["album_name", "band_name", "price", "year"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["user_id", "status", "address", "time"]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order_id", "item_id"]


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
