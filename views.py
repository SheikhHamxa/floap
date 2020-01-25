from django.shortcuts import render


from rest_framework import generics, permissions


from location.models import Franchise, LocationType
from .permissions import IsOwnerOrReadOnly  # new

from .models import Location
from .serializations import LocationSerializer, LocationTypeSerializer
from .serializations import FranchiseSerializer

"""
class LocationHighlight(generics.GenericAPIView):
    queryset = Location.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
"""


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class LocationTypeList(generics.ListCreateAPIView):
    queryset = LocationType.objects.all()
    serializer_class = LocationTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LocationTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocationType.objects.all()
    serializer_class = LocationTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


""""

class FranchiseTypeList(generics.ListAPIView):
    queryset = FranchiseType.objects.all()
    serializer_class = FranchiseTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FranchiseTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FranchiseType.objects.all()
    serializer_class = FranchiseTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

"""


class FranchiseList(generics.ListCreateAPIView):
    queryset = Franchise.objects.all()
    serializer_class = FranchiseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FranchiseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Franchise.objects.all()
    serializer_class = FranchiseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
