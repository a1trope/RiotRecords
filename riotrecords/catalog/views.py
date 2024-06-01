from django.http import HttpResponse
from django.shortcuts import render
from .models import Item


def index(request):
    return render(request, "catalog/index.html", context={"Items": Item.objects.all()})

def detail(request, item_id):
    # return render(request, "catalog/detail.html", context={"Items": Item.objects.all()})
    return HttpResponse(f"You are looking at item {item_id}")
