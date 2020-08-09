"""This module manages the views of the categories app."""
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from providers.models import Provider
from providers.serializers import ProviderListSerializer, ProviderSerializer


class ProviderView(APIView):
    """
    This class manages the view to create and list the providers.

    Attributes:
        permission_classes (list(Permissions)): The options to access at this resource.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Retrieve the providers list.

        Attributes:
            request (Request): The request sent to the api.
            format (NoneType): Always none, pass by Accept header.

        Returns:
            200: The list of providers.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
        """
        providers = Provider.objects.filter(owner=request.user)  # pylint: disable=no-member
        serializer = ProviderListSerializer(providers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a provider.

        Attributes:
            request (Request): The request sent to the api.
            format (NoneType): Always none, pass by Accept header.

        Returns:
            201: The provider is created.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
        """
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class manages the view to update and delete a provider.

    Attributes:
        permission_classes (list(Permissions)): The options to access at this resource.
        serializer_class (Serializer): The serializer to bind the request and the response object.

    Returns:
            200: The provider is updated.
            204: The provider is deleted.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProviderSerializer

    def get_queryset(self):
        """Return the category of the owner."""
        return Provider.objects.filter(owner=self.request.user, pk=self.kwargs['pk'])  # pylint: disable=no-member

    def perform_update(self, serializer):
        """Update the owner of the category before update it."""
        serializer.save(owner=self.request.user)
