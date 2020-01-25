
from django.shortcuts import render

from rest_framework import generics, permissions

from .permissions import IsOwnerOrReadOnly

from .models import Package, PackageStatus, PackageRates, PackageBilling
from .serializations import PackageSerializer, PackageStatusSerializer, PackageRatesSerializer, PackageBillingSerializer

"""
class PackageHighlight(generics.GenericAPIView):
    queryset = Package.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
"""


class PackageList(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PackageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class PackageStatusList(generics.ListCreateAPIView):
    queryset = PackageStatus.objects.all()
    serializer_class = PackageStatusSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PackageStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PackageStatus.objects.all()
    serializer_class = PackageStatusSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class PackageRatesList(generics.ListCreateAPIView):
    queryset = PackageRates.objects.all()
    serializer_class = PackageRatesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PackageRatesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PackageRates.objects.all()
    serializer_class = PackageRatesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class PackageBillingList(generics.ListCreateAPIView):
    queryset = PackageBilling.objects.all()
    serializer_class = PackageBillingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PackageBillingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PackageBilling.objects.all()
    serializer_class = PackageBillingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

