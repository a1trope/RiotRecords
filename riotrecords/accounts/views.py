from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("catalog:index")
        else:
            return render(request, "accounts/login.html", context={
                "error_msg": f"Пользователя \"{username}\" с данным паролем не существует. Попробуйте ещё раз."
            })

    return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    return redirect("catalog:index")
