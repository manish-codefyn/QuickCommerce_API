from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileView,
    AddressListCreateView,
    AddressDetailView,
    SetDefaultAddressView,
)

router = DefaultRouter()

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('addresses/', AddressListCreateView.as_view(), name='address-list'),
    path('addresses/<uuid:pk>/', AddressDetailView.as_view(), name='address-detail'),
    path('addresses/<uuid:pk>/set-default/', SetDefaultAddressView.as_view(), name='set-default-address'),
]

urlpatterns += router.urls