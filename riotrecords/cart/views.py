from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from catalog.models import Item
from django.contrib.auth.decorators import login_required

@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items})

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'catalog/detail.html', {'item': item})
