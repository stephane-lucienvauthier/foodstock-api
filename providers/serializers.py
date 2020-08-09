"""This module defines the serializers for the providers app."""
from rest_framework import serializers
from providers.models import Provider


class ProviderListSerializer(serializers.ModelSerializer):
    """This class defines the serializer for the providers list view."""

    class Meta:
        """
         This class defines the validation metadata for the providers list view.
        
        Attributes:
            model (Model): The model linked to the serializer.
            fields (list(str)): The field list expencted by the serializer.
        """

        model = Provider
        fields = ['id', 'label', 'city']

class ProviderSerializer(serializers.ModelSerializer):
    """This class defines the serializer for the providers other views."""

    class Meta:
        """
         This class defines the validation metadata for the providers other views.
        
        Attributes:
            model (Model): The model linked to the serializer.
            fields (list(str)): The field list expencted by the serializer.
        """

        model = Provider
        fields = ['id', 'label', 'address', 'city', 'zipcode', 'phone']
