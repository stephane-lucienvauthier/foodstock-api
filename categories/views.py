"""This module manages the views of the categories app."""
from rest_framework import generics, permissions
from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryView(generics.ListCreateAPIView):
    """
    This class manages the view to create and list the categories.

    Attributes:
        permission_classes (list(Permissions)): The options to access at this resource.
        serializer_class (Serializer): The serializer to bind the request and the response object.

    Returns:
            200: The list of categories.
            201: The category is created.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request. 
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self):
        """Return the category list of the owner."""
        return Category.objects.filter(owner=self.request.user)  # pylint: disable=no-member

    def perform_create(self, serializer):
        """Add the owner of the category before create it."""
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class manages the view to update and delete a category.

    Attributes:
        permission_classes (list(Permissions)): The options to access at this resource.
        serializer_class (Serializer): The serializer to bind the request and the response object.

    Returns:
            200: The category is updated.
            204: The category is deleted.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self):
        """Return the category of the owner."""
        return Category.objects.filter(owner=self.request.user, pk=self.kwargs['pk'])  # pylint: disable=no-member

    def perform_update(self, serializer):
        """Update the owner of the category before update it."""
        serializer.save(owner=self.request.user)
