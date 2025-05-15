from django.urls import path
from .views import (
    OrderListView,
    OrderDetailView,
    CartDetailView,
    CartItemCreateView,
    CartItemUpdateDestroyView,
    CheckoutView,
    OrderCancelView,
)

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<uuid:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<uuid:pk>/cancel/', OrderCancelView.as_view(), name='order-cancel'),
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('cart/items/', CartItemCreateView.as_view(), name='cart-item-create'),
    path('cart/items/<uuid:pk>/', CartItemUpdateDestroyView.as_view(), name='cart-item-detail'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]