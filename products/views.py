"""This module manages the views of the categories app."""
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product, Batch
from products.serializers import ProductSerializer, ProductUpdateSerializer, ProductListSerializer, BatchSerializer


class ProductView(APIView):
    """
    This class manages the view to create and list the products.

    Attributes:
        permission_classes (list(Permissions)): The options to access at this resource.
        serializer_class (Serializer): The serializer to bind the request and the response object.

    Returns:
            200: The list of products.
            201: The product is created.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request. 
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Retrieve the product list with batches in stock.

        Attributes:
            request (Request): The request sent to the api.
            format (NoneType): Always none, pass by Accept header.

        Returns:
            200: The product is updated.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
        """
        products = Product.objects.filter(owner=request.user) # pylint: disable=no-member
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a product.

        Attributes:
            request (Request): The request sent to the api.
            format (NoneType): Always none, pass by Accept header.

        Returns:
            201: The product is created.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
        """
        serializer = ProductUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """
    This class manages the view to update and delete a product.

    Attributes:
        permission_classes (list(Permissions)): The options to access at this resource.
        serializer_class (Serializer): The serializer to bind the request and the response object.

    Returns:
            200: The product is updated.
            204: The product is deleted.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        """
        Retrieve a batch.

        Attributes:
            request (Request): The request sent to the api.
            pk (int): The product identifier.
            format (NoneType): Always none, pass by Accept header.

        Returns:
            200: The product is updated.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
        """
        try:
            product = Product.objects.get(owner=request.user, pk=pk) # pylint: disable=no-member
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update a product.

        Attributes:
            request (Request): The request sent to the api.
            pk (int): The product identifier.
            format (NoneType): Always none, pass by Accept header.

        Returns:
            200: The product is updated.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
        """
        product = Product.objects.get(owner=request.user, pk=pk) # pylint: disable=no-member
        serializer = ProductUpdateSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete a product.

        Attributes:
            request (Request): The request sent to the api.
            pk (int): The product identifier.
            ps (int): the batch identifier.
            format (NoneType): Always none, pass by Accept header.

        Returns:
            204: The product is deleted.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
        """
        product = Product.objects.get(owner=request.user, pk=pk) # pylint: disable=no-member
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BatchView(generics.ListCreateAPIView):
    """
    This class manages the view to create and list the products.

    Attributes:
        permission_classes (list(Permissions)): The options to access at this resource.
        serializer_class (Serializer): The serializer to bind the request and the response object.

    Returns:
            200: The list of products.
            201: The product is created.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request. 
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BatchSerializer

    def get_queryset(self):
        """Return the category list of the owner."""
        product = Product.objects.get(owner=self.request.user, pk=self.kwargs['pk']) # pylint: disable=no-member
        return Batch.objects.filter(owner=self.request.user, product=product)  # pylint: disable=no-member

    def perform_create(self, serializer):
        """Add the owner of the category before create it."""
        product = Product.objects.get(owner=self.request.user, pk=self.kwargs['pk']) # pylint: disable=no-member
        serializer.save(owner=self.request.user, product=product)


class BatchDetail(APIView):
    """
    This class manages the view to update and delete a batch.

    Attributes:
        permission_classes (list(Permissions)): The options to access at this resource.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, ps, format=None):
        """
        Retrieve a batch.

        Attributes:
            request (Request): The request sent to the api.
            pk (int): The product identifier.
            ps (int): the batch identifier.
            format (NoneType): Always none, pass by Accept header.

        Returns:
            200: The product is updated.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
        """
        product = Product.objects.get(owner=request.user, pk=pk) # pylint: disable=no-member
        try:
            batch = Batch.objects.get(owner=request.user, product=product, pk=ps)  # pylint: disable=no-member
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BatchSerializer(batch)
        return Response(serializer.data)

    def put(self, request, pk, ps, format=None):
        """
        Update a batch.

        Attributes:
            request (Request): The request sent to the api.
            pk (int): The product identifier.
            ps (int): the batch identifier.
            format (NoneType): Always none, pass by Accept header.

        Returns:
            200: The product is updated.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
        """
        product = Product.objects.get(owner=request.user, pk=pk) # pylint: disable=no-member
        batch = Batch.objects.get(owner=request.user, product=product, pk=ps)  # pylint: disable=no-member

        serializer = BatchSerializer(batch, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user, product=product)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, ps, format=None):
        """
        Delete a batch.

        Attributes:
            request (Request): The request sent to the api.
            pk (int): The product identifier.
            ps (int): the batch identifier.
            format (NoneType): Always none, pass by Accept header.

        Returns:
            204: The product is deleted.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
        """
        product = Product.objects.get(owner=request.user, pk=pk) # pylint: disable=no-member
        batch = Batch.objects.get(owner=request.user, product=product, pk=ps)  # pylint: disable=no-member
        batch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
