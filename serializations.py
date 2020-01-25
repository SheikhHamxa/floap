from rest_framework import serializers
from location.models import Franchise
from package.models import PackageRates
from vehicle.models import Vehicle
from vehicle.serializations import VehicleSerializer
from .models import USer
# from .models import Sender
from .models import UserType
# from .models import Receiver
# from .models import Manager
# from .models import PostPerson
# from .models import Staff

from django.contrib.auth.models import User


class USerSerializer(serializers.ModelSerializer):
    #  sender = serializers.StringRelatedField(many=True)
    #  receiver = serializers.StringRelatedField(many=True)
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    usertype = serializers.SlugRelatedField(queryset=UserType.objects.all(), slug_field='user_type')
    franchise = serializers.SlugRelatedField(queryset=Franchise.objects.all(), slug_field='name')
    # vehicle=serializers.StringRelatedField(many=True)
    # "" packagerates = serializers.SlugRelatedField(queryset=PackageRates.objects.all(), slug_field='price_per_gram')
    # postperson = serializers.StringRelatedField(many=True, read_only=True)
    # manager = serializers.StringRelatedField(many=True, read_only=True)
    # staff = serializers.StringRelatedField(many=True, read_only=True)
    # package = serializers.StringRelatedField(many=True, read_only=True)
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = USer
        fields = '__all__'


class UserTypeSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user = serializers.StringRelatedField(many=True, read_only=True)
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = UserType
        fields = '__all__'

"""
class SenderSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    receievr = serializers.StringRelatedField()

    class Meta:
        model = Sender
        fields = '__all__'


class ReceiverSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Receiver
        fields = '__all__'

"""
"""
class PostPersonSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = PostPerson
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Manager
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Staff
        fields = '__all__'
"""
