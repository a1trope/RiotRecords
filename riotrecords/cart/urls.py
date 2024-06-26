from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('delete/<int:cartitem_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('order/', views.order, name='order'),
]
