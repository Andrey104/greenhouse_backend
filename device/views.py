from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from device.models import MainDevice
from device.serializers import DeviceSerializer
from greenhouse_backend.utils import CRUModelViewSet


class DeviceViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    serializer_class = DeviceSerializer
    pagination_class = None

    def get_queryset(self):
        return MainDevice.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
