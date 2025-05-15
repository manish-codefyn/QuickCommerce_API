from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Payment, Refund
from .serializers import (
    PaymentSerializer,
    PaymentCreateSerializer,
    RefundSerializer,
    RefundCreateSerializer,
)
from orders.models import Order
from users.permissions import IsOrderOwner


class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentCreateSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrderOwner]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['order'] = get_object_or_404(
            Order,
            id=self.kwargs['order_id'],
            user=self.request.user
        )
        return context
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment = serializer.save()
        
        # Process payment (this would integrate with your payment gateway)
        # For now, we'll just mark it as completed
        payment.status = Payment.Status.COMPLETED
        payment.save()
        
        # Update order status
        payment.order.status = Order.Status.PROCESSING
        payment.order.save()
        
        return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)


class PaymentDetailView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrderOwner]
    
    def get_queryset(self):
        return Payment.objects.filter(order__user=self.request.user)


class RefundCreateView(generics.CreateAPIView):
    serializer_class = RefundCreateSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrderOwner]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        payment = get_object_or_404(
            Payment,
            id=self.kwargs['payment_id'],
            order__user=self.request.user
        )
        context['payment'] = payment
        return context
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refund = serializer.save()
        
        # Process refund (this would integrate with your payment gateway)
        # For now, we'll just mark it as completed
        refund.status = Payment.Status.COMPLETED
        refund.save()
        
        # Update payment status
        refund.payment.status = Payment.Status.REFUNDED
        refund.payment.save()
        
        return Response(RefundSerializer(refund).data, status=status.HTTP_201_CREATED)


class RefundListView(generics.ListAPIView):
    serializer_class = RefundSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrderOwner]
    
    def get_queryset(self):
        return Refund.objects.filter(payment__order__user=self.request.user)


class RefundDetailView(generics.RetrieveAPIView):
    serializer_class = RefundSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrderOwner]
    
    def get_queryset(self):
        return Refund.objects.filter(payment__order__user=self.request.user)