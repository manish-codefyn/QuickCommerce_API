from rest_framework import generics, permissions
from .models import Report, Dashboard
from .serializers import ReportSerializer, DashboardSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from orders.models import Order
from products.models import Product
from users.models import User


class ReportListView(generics.ListCreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def get_queryset(self):
        return Report.objects.all()
    
    def perform_create(self, serializer):
        report = serializer.save()
        # In a real implementation, you would trigger a Celery task here
        # For now, we'll just simulate it
        report.is_ready = True
        report.save()


class ReportDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Report.objects.all()


class DashboardListView(generics.ListCreateAPIView):
    serializer_class = DashboardSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Dashboard.objects.all()


class DashboardDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DashboardSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Dashboard.objects.all()


class SalesSummaryView(generics.GenericAPIView):
    permission_classes = [permissions.IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        # Get time range (default to last 30 days)
        days = int(request.query_params.get('days', 30))
        end_date = timezone.now()
        start_date = end_date - timedelta(days=days)
        
        # Get sales data
        orders = Order.objects.filter(
            created_at__range=(start_date, end_date),
            status__in=[Order.Status.DELIVERED, Order.Status.PROCESSING, Order.Status.SHIPPED]
        )
        
        total_sales = sum(order.total_amount for order in orders)
        total_orders = orders.count()
        
        # Get popular products
        popular_products = Product.objects.filter(
            order_items__order__in=orders
        ).annotate(
            total_sold=models.Sum('order_items__quantity')
        ).order_by('-total_sold')[:5]
        
        # Get new customers
        new_customers = User.objects.filter(
            is_customer=True,
            date_joined__range=(start_date, end_date)
        ).count()
        
        data = {
            'time_range': {
                'start': start_date,
                'end': end_date,
                'days': days
            },
            'total_sales': total_sales,
            'total_orders': total_orders,
            'new_customers': new_customers,
            'popular_products': [
                {'name': p.name, 'total_sold': p.total_sold}
                for p in popular_products
            ]
        }
        
        return Response(data)