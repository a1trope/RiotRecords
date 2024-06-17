from django.shortcuts import render, get_object_or_404
from .models import Item
from cart.forms import AddToCartForm

def index(request):
    return render(request, "catalog/index.html", context={"Items": Item.objects.all()})

def detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = AddToCartForm()
    return render(request, "catalog/detail.html", {'item': item, 'form': form})
