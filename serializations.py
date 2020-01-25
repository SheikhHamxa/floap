from rest_framework import serializers

from location.models import Franchise
from .models import Vehicle, VehicleType
from django.contrib.auth.models import User


class VehicleSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    vehicle_type= serializers.SlugRelatedField(queryset=VehicleType.objects.all(), slug_field='vehicle_type')
    franchise = serializers.SlugRelatedField(queryset=Franchise.objects.all(), slug_field='name')
    # user = serializers.SlugRelatedField(queryset=USer.objects.all(), slug_field='first_name')
    #user = serializers.StringRelatedField(many=True, read_only=True)
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # package = serializers.StringRelatedField(many=True,read_only=True)

    # user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleTypeSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # USer = serializers.StringRelatedField(many=True, read_only=True)
    # package = serializers.StringRelatedField(many=True, read_only=True)
    # location = serializers.StringRelatedField(many=True, read_only=True)
    # package = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = VehicleType
        fields = '__all__'

