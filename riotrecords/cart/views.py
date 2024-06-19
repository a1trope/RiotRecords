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
    user = request.user

    cart_item = CartItem.objects.create(user=user, item=item)
    cart_item.save()

    return redirect("catalog:index")


@login_required
def delete_from_cart(request, cartitem_id):
    user = request.user
    cart_item = get_object_or_404(CartItem, id=cartitem_id, user=user)
    cart_item.delete()

    return redirect("cart:cart_detail")