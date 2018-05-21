from datetime import datetime

from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route, action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from device.models import MainDevice, SensorsData
from device.serializers import DeviceSerializer, SensorsDataSerializer
from greenhouse_backend.utils import CRUModelViewSet, transaction_atomic
from greenhouse_backend.views import get_object_data, create_object


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

    @action(methods=['post'], detail=False, url_path='sync', permission_classes=(AllowAny,))
    def sync(self, request, pk=None):
        device_code = request.data["code"]
        main_device = MainDevice.objects.get(device_code=device_code)
        main_device.last_sync = datetime.now().isoformat()
        main_device.save()
        return Response(device_code)

    @staticmethod
    def deal_validate(main_device):
        if not main_device:
            raise ValidationError(dict(detail='Device not registered!'))
