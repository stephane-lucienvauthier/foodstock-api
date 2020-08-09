"""This module defines the routes for the categories resources."""
from django.urls import path
from providers.views import ProviderView, ProviderDetail

urlpatterns = [
    path('', ProviderView.as_view()),
    path('<int:pk>', ProviderDetail.as_view())
]
