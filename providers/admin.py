"""This module manages the admin section for the providers app."""
from django.contrib import admin
from .models import Provider

admin.site.register(Provider)
