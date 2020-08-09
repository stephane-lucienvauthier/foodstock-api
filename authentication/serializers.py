"""This module defines the serializers for the authentication app."""
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    """This class defines the serializer for the register view."""

    def to_representation(self, obj):
        """Format the representation to send result."""
        representation = super(RegisterSerializer, self).to_representation(obj)
        representation.pop('password')
        return representation

    class Meta:
        """
        This class defines the validation metadata for the register view.
        
        Attributes:
            model (Model): The model linked to the serializer.
            fields (list(str)): The field list expencted by the serializer.
        """

        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
