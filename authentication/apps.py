"""This module defines the configuration for the authentication app."""
from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    This class defines the configuration for the authentication app.

    Attributes:
        name (str): The app name.
    """
    name: str = 'authentication'
