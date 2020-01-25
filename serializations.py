from rest_framework import serializers
from .models import Location, LocationType


from django.contrib.auth.models import User
from django.db import models

from location.models import Franchise


class LocationSerializer(serializers.ModelSerializer):
    # user= serializers.StringRelatedField(many=True, read_only=True)
    # packagerates= serializers.StringRelatedField(many=True, read_only=True)
    location_type = serializers.SlugRelatedField(queryset=LocationType.objects.all(), slug_field='type')
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    # franchise= serializers.StringRelatedField(many=True, read_only=True)
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Location
        fields = '__all__'


class LocationTypeSerializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField(read_only=True, many=True)
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = LocationType
        fields = '__all__'


class FranchiseSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    location = serializers.SlugRelatedField(queryset=Location.objects.all(), slug_field='house_no')
    # user = serializers.StringRelatedField(many=True, read_only=True)
    # vehicle = serializers.StringRelatedField(many=True, read_only=True)
    # packagebilling = serializers.StringRelatedField(many=True, read_only=True)
    # location = models.OneToOneField(Location, related_name='franchise',on_delete=models.CASCADE)


    class Meta:
        model = Franchise
        fields = '__all__'


"""
class FranchiseTypeSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = FranchiseType
        fields='__all__'
"""
