from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            # TODO: show errors if can't find user
            return render(request, "accounts/login.html")

    return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    return redirect("catalog:index")
