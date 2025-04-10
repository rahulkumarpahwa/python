from django.contrib.auth.models import User
from rest_framework import serializers
from .models import GeoLocation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "deviceID", "name", "email"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class GeoLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoLocation
        fields = ["id", "latitude", "longitude", "timestamp", "location_name" ]
        extra_kwargs = {"author": {"read_only": True}}