from django.urls import path
from .views import (
    PaymentCreateView,
    PaymentDetailView,
    RefundCreateView,
    RefundListView,
    RefundDetailView,
)

urlpatterns = [
    path('orders/<uuid:order_id>/payment/', PaymentCreateView.as_view(), name='payment-create'),
    path('payments/<uuid:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('payments/<uuid:payment_id>/refunds/', RefundCreateView.as_view(), name='refund-create'),
    path('refunds/', RefundListView.as_view(), name='refund-list'),
    path('refunds/<uuid:pk>/', RefundDetailView.as_view(), name='refund-detail'),
]