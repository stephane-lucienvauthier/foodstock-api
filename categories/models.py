"""This module defines the models of the categories app."""
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    This class defines the category model.

    Attributes:
        owner (User): The category owner.
        label (str):  The category label.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    
    def __str__(self):
        """Return the value when the model is called directly."""
        return self.label

    class Meta:
        """
        This class defines metadata for the model.

        Attributes:
            ordering (list(str)): The list to sort a list of models.
        """

        ordering = ['label']