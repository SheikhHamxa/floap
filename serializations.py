from rest_framework import serializers
from django.db import models

from location.models import Location, Franchise
from vehicle.models import Vehicle
from .models import Package, PackageRates, PackageStatus, PackageBilling

from django.contrib.auth.models import User
from USer.models import USer


class PackageSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    packagerates = serializers.SlugRelatedField(queryset=PackageRates.objects.all(), slug_field='price_per_gram')
    user= serializers.SlugRelatedField(queryset=USer.objects.all(), slug_field='first_name')
    packagestatus= serializers.SlugRelatedField(queryset=PackageStatus.objects.all(), slug_field='status')
    # vehicle = serializers.SlugRelatedField(queryset=Vehicle.objects.all(), slug_field='name')
    # usertype = serializers.StringRelatedField(many=True, read_only=True)
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # packagestatus = serializers.StringRelatedField(many=True,read_only=True)
    # user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Package
        fields = '__all__'


class PackageBillingSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    franchise= serializers.SlugRelatedField(queryset=Franchise.objects.all(), slug_field='email')
    package= serializers.SlugRelatedField(queryset=Package.objects.all(), slug_field='name')
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = PackageBilling
        fields = '__all__'


class PackageRatesSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # user = serializers.StringRelatedField(many=True, read_only=True)
    # package = serializers.StringRelatedField(many=True, read_only=True)
    # location = serializers.SlugRelatedField(queryset=Location.objects.all(), slug_field='house_no')

    # location = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = PackageRates
        fields = '__all__'


class PackageStatusSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    # package = serializers.SlugRelatedField(queryset=Package.objects.all(), slug_field='name')

    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # franchise = models.OneToOneField(PackageRates, related_name='packagerates', on_delete=models.CASCADE)

    class Meta:
        model = PackageStatus
        fields = '__all__'
