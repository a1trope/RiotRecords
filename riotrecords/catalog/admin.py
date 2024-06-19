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

    def changeform_view(self, request, *args, **kwargs):
        if not request.user.is_superuser and request.user.groups.filter(name="Stuff").exists():
            self.readonly_fields = ["user", "address", "time"]

        return super(OrderAdmin, self).changeform_view(request, *args, **kwargs)


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
