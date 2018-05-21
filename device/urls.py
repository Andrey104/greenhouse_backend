from django.urls import path, include
from rest_framework.routers import DefaultRouter

from device.views import DeviceViewSet

router = DefaultRouter()
router.register('', DeviceViewSet, base_name='device')

urlpatterns = [
    path('', include(router.urls)),
]