"""This module defines the serializers for the categories app."""
from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """This class defines the serializer for the categories view."""

    class Meta:
        """
         This class defines the validation metadata for the categories view.
        
        Attributes:
            model (Model): The model linked to the serializer.
            fields (list(str)): The field list expencted by the serializer.
        """

        model = Category
        fields = ['id', 'label']
