"""This module manages the admin section for the categories app."""
from django.contrib import admin
from .models import Category

admin.site.register(Category)