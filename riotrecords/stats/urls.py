from django.urls import path, include

from . import views

app_name = "stats"
urlpatterns = [
    path("", views.get_total_sales, name="get_total_sales"),
    path("<int:item_id>/", views.get_stats, name="get_stats"),
]
