from django.contrib import admin
from .models import Item, Order, OrderItem


class ItemAdmin(admin.ModelAdmin):
    list_display = ["album_name", "band_name", "price", "year"]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order_id", "item_id"]


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "status", "address", "time"]
    inlines = [OrderItemAdminInline]


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
