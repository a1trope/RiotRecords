from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect("/admin")
            else:
                return redirect("catalog:index")
        else:
            return render(request, "accounts/login.html", context={
                "error_msg": f"Пользователя \"{username}\" с данным паролем не существует. Попробуйте ещё раз."
            })

    return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    return redirect("catalog:index")


def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect("catalog:index")
        else:
            return render(request, "accounts/registration.html", context={
                "error_msg": f"Ошибка регистрации. Пользователь с таким \"{username}\" уже существует."
            })

    return render(request, "accounts/registration.html")
