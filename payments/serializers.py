from rest_framework import serializers
from .models import Payment, Refund
from orders.serializers import OrderSerializer


class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    
    class Meta:
        model = Payment
        fields = [
            'id', 'order', 'amount', 'method', 'status',
            'transaction_id', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'order', 'amount', 'created_at', 'updated_at']


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['method', 'payment_details']
    
    def validate(self, data):
        order = self.context['order']
        if hasattr(order, 'payment'):
            raise serializers.ValidationError("This order already has a payment.")
        return data
    
    def create(self, validated_data):
        order = self.context['order']
        payment = Payment.objects.create(
            order=order,
            amount=order.total_amount,
            **validated_data
        )
        return payment


class RefundSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(read_only=True)
    
    class Meta:
        model = Refund
        fields = ['id', 'payment', 'amount', 'reason', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'payment', 'status', 'created_at', 'updated_at']


class RefundCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = ['amount', 'reason']
    
    def validate_amount(self, value):
        payment = self.context['payment']
        if value > payment.amount:
            raise serializers.ValidationError("Refund amount cannot exceed payment amount.")
        return value
    
    def create(self, validated_data):
        payment = self.context['payment']
        refund = Refund.objects.create(
            payment=payment,
            **validated_data
        )
        return refund