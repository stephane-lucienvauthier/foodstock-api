"""This module defines the serializers for the products app."""
from rest_framework import serializers
from products.models import Product, Batch


class BatchSerializer(serializers.ModelSerializer):
    """This class defines the serializer for the batches view."""

    def to_representation(self, obj):
        """Format the representation to send result."""
        representation = super(BatchSerializer, self).to_representation(obj)
        representation['provider'] = obj.provider.label
        return representation

    class Meta:
        """
         This class defines the validation metadata for the batches view.
        
        Attributes:
            model (Model): The model linked to the serializer.
            fields (list(str)): The field list expencted by the serializer.
        """

        model = Batch
        fields = ['id', 'initial', 'current', 'price', 'purchase', 'limit', 'provider']


class ProductUpdateSerializer(serializers.ModelSerializer):
    """This class defines the serializer for the products view."""

    def to_representation(self, obj):
        """Format the representation to send result."""
        representation = super(ProductUpdateSerializer, self).to_representation(obj)
        representation['category'] = obj.category.label
        return representation

    class Meta:
        """
         This class defines the validation metadata for the products view.
        
        Attributes:
            model (Model): The model linked to the serializer.
            fields (list(str)): The field list expencted by the serializer.
        """

        model = Product
        fields = ['id', 'label', 'unit', 'category', 'icon']


class ProductSerializer(serializers.ModelSerializer):
    """This class defines the serializer for the products view."""

    batches = BatchSerializer(many=True, read_only=True)
    
    def to_representation(self, obj):
        """Format the representation to send result."""
        representation = super(ProductSerializer, self).to_representation(obj)
        representation['category'] = obj.category.label
        return representation

    class Meta:
        """
         This class defines the validation metadata for the products view.
        
        Attributes:
            model (Model): The model linked to the serializer.
            fields (list(str)): The field list expencted by the serializer.
        """

        model = Product
        fields = ['id', 'label', 'unit', 'category', 'icon', 'batches']

class ProductListSerializer(ProductSerializer):
    """This class defines the serializer for the products view."""
    
    def to_representation(self, obj):
        """Format the representation to send result."""
        representation = super(ProductListSerializer, self).to_representation(obj)
        representation["batches"] = list(filter(lambda x: x["current"] > 0, representation["batches"]))
        representation['category'] = obj.category.label
        return representation
