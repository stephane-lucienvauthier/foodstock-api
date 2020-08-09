"""This module defines the models of the products app."""
from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from providers.models import Provider


class Product(models.Model):
    """
    This class defines the product model.

    Attributes:
        owner (User): The product owner.
        category (Category): the product category.
        label (str):  The product label.
        unit (str): The product unit.
        icon (str): The product icon.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    icon = models.TextField(null=True)
    
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


"""This module defines the models of the products app."""
from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


class Batch(models.Model):
    """
    This class defines the batch model.

    Attributes:
        owner (User): The batch owner.
        product (Product): the linked product.
        provider (Provider): The linked provider.
        initial (float):  The initial quantity.
        current (float): The current quantity.
        price (float): The Batch unit price.
        purchase (Date): The date of purchase.
        limit (Date): The DLUO.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='batches', on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    initial = models.FloatField(default=0.0)
    current = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    purchase = models.DateField()
    limit = models.DateField()
    
    def __str__(self):
        """Return the value when the model is called directly."""
        return str(self.current)

    class Meta:
        """
        This class defines metadata for the model.

        Attributes:
            ordering (list(str)): The list to sort a list of models.
        """

        ordering = ['limit', 'current']
