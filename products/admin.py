"""This module manages the admin section for the products app."""
from django.contrib import admin
from .models import Product, Batch

admin.site.register(Product)
admin.site.register(Batch)
