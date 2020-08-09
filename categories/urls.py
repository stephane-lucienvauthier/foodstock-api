"""This module defines the routes for the categories resources."""
from django.urls import path
from categories.views import CategoryView, CategoryDetail

urlpatterns = [
    path('', CategoryView.as_view()),
    path('<int:pk>', CategoryDetail.as_view())
]
