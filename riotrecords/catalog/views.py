from django.shortcuts import render, get_object_or_404
from .models import Item

def index(request):
    return render(request, "catalog/index.html", context={"Items": Item.objects.all()})
