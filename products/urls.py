"""This module defines the routes for the products resources."""
from django.urls import path
from products.views import ProductView, ProductDetail, BatchView, BatchDetail

urlpatterns = [
    path('', ProductView.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
    path('<int:pk>/batches/', BatchView.as_view()),
    path('<int:pk>/batches/<int:ps>', BatchDetail.as_view())
]
