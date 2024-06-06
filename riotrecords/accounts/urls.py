from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("login_user", views.login, name="login"),
    path("logout_user", views.logout, name="logout"),
]