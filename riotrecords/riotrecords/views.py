from django.shortcuts import render, redirect


def handle_404_error(request, exception):
    return redirect("accounts:login")
