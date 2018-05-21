from django.contrib.auth.models import User
from rest_framework import serializers

from device.models import MainDevice, SensorsData


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainDevice
        fields = '__all__'
        read_only_fields = ('user',)


class SensorsDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorsData
        fields = '__all__'
        read_only_fields = ('user',)

