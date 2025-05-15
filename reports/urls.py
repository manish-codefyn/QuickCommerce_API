from django.urls import path
from .views import (
    ReportListView,
    ReportDetailView,
    DashboardListView,
    DashboardDetailView,
    SalesSummaryView,
)

urlpatterns = [
    path('reports/', ReportListView.as_view(), name='report-list'),
    path('reports/<uuid:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('dashboards/', DashboardListView.as_view(), name='dashboard-list'),
    path('dashboards/<uuid:pk>/', DashboardDetailView.as_view(), name='dashboard-detail'),
    path('sales-summary/', SalesSummaryView.as_view(), name='sales-summary'),
]