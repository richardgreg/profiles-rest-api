from django.shortcuts import render

from rest_framework import viewsets # Base model for rstfrmwrk views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
# Import for login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from django_filters.rest_framework import DjangoFilterBackend

from . import serializers
from . import models
from . import permissions

# Create your views here.
class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API view functions"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with name"""

        serializer = serializers.HelloSerializer(data=request.data)

        # Retrieve the data (name) if valid.
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating object"""

        return Response({'method: put'})

    def patch(self, request, pk=None):
        """Patch requests, only updates fields provided in the request"""

        return Response({'method: patch'})

    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({'method: delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns a message"""
        a_viewset = [
        'Uses actions (list, create, update, retrieve, partial update, destroy)',
        'Auto maps to urls using routers',
        'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HelloSerializer(data=request.data)

        # Retrieve the data (name) if valid.
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        
        return Response({'http_method': 'DELETE'})

     
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating reading and updating profiles"""

    serializer_class = serializers.UserProfileSerializer

    # Queryset for how to retrieve objects from database
    queryset = models.UserProfile.objects.all()

    # A tuple containing all the authentication class that will be used by API
    authentication_classes = (TokenAuthentication,)

    # A tuple containing all the permission class that will be used by API
    permission_classes = (permissions.UpdateOwnProfile,)

    # A tuple containing all the filter class that will be used by API
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)

    search_fields = ['name', 'email',]


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken API view to validate and create a token"""

        return ObtainAuthToken().post(request)

