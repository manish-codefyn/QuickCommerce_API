from django.urls import path
from .views import (
    NotificationListView,
    NotificationDetailView,
    UnreadNotificationCountView,
)

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('<uuid:pk>/', NotificationDetailView.as_view(), name='notification-detail'),
    path('unread-count/', UnreadNotificationCountView.as_view(), name='unread-count'),
]