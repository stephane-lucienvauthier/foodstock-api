"""This module defines the models of the providers app."""
from django.db import models
from django.contrib.auth.models import User


class Provider(models.Model):
    """
    This class defines the provider model.

    Attributes:
        owner (User): The provider owner.
        label (str):  The provider label.
        address (str): The provider adress.
        city (str): The provider city.
        zipcode (str): The provider zipcode.
        phone (str): The provider phone number.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)

    def __str__(self):
        """Return the value when the model is called directly."""
        return f"{self.label} - {self.city}"

    class Meta:
        """
        This class defines metadata for the model.

        Attributes:
            ordering (list(str)): The list to sort a list of models.
        """

        ordering = ['label', 'city']
