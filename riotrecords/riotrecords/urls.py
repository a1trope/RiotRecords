from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("catalog.urls")),
    path('accounts/', include("accounts.urls")),
    path('cart/', include("cart.urls")),
    path('stats/', include("stats.urls")),
]

handler404 = 'riotrecords.views.handle_404_error'
