from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from catalog.models import Item
from .forms import AddToCartForm
from django.contrib.auth.decorators import login_required

@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items})

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            cart_item, created = CartItem.objects.get_or_create(user=request.user, item=item)
            if not created:
                cart_item.quantity += form.cleaned_data['quantity']
            else:
                cart_item.quantity = form.cleaned_data['quantity']
            cart_item.save()
            return redirect('cart_detail')
    else:
        form = AddToCartForm()
    return render(request, 'catalog/detail.html', {'form': form, 'item': item})
