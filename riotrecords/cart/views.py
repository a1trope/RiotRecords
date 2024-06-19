from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from catalog.models import Item, Order, OrderItem
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import CartItem


@login_required(login_url="accounts:login")
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items})


@login_required(login_url="accounts:login")
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    user = request.user

    cart_item = CartItem.objects.create(user=user, item=item)
    cart_item.save()

    return redirect("catalog:index")


@login_required(login_url="accounts:login")
def delete_from_cart(request, cartitem_id):
    user = request.user
    cart_item = get_object_or_404(CartItem, id=cartitem_id, user=user)
    cart_item.delete()

    return redirect("cart:cart_detail")


@login_required(login_url="accounts:login")
def order(request):
    if request.method == "POST":
        user = request.user
        address = request.POST["address"]

        # Get user cart items
        cart_items = CartItem.objects.filter(user=user)

        if len(cart_items) < 1:
            return render(request, 'cart/order.html', {'error_msg': "У вас пустая корзина"})

        # Create order
        order = Order.objects.create(user=user, address=address)
        order.save()

        # Create order items
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(order=order, item=cart_item.item)
            order_item.save()

        # Clear cart for current user
        cart_items.delete()

        return render(request, 'cart/success_order.html')

    form = OrderForm()
    return render(request, 'cart/order.html', {'form': form})

