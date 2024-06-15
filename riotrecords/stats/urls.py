from django.urls import path

from . import views

app_name = "stats"
urlpatterns = [
    path("", views.get_total_sales, name="get_total_sales"),
]
