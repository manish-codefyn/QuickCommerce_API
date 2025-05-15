from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    ProductListCreateView,
    ProductDetailView,
    ProductReviewListCreateView,
    ProductReviewDetailView,
)

router = DefaultRouter()

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<slug:slug>/reviews/', ProductReviewListCreateView.as_view(), name='product-review-list'),
    path('products/<slug:slug>/reviews/<uuid:pk>/', ProductReviewDetailView.as_view(), name='product-review-detail'),
]

urlpatterns += router.urls