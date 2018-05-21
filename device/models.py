from django.contrib.auth.models import User
from django.db import models


class MainDevice(models.Model):
    name = models.TextField(max_length=120)
    device_code = models.TextField(max_length=6, unique=True)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    last_sync = models.DateTimeField(null=True)


class SlaveDevice(models.Model):
    name = models.TextField(max_length=120)
    description = models.TextField()
    main = models.ForeignKey(MainDevice, on_delete=models.CASCADE)


class Sensor(models.Model):
    name = models.TextField(max_length=120)
    sensor_code = models.IntegerField()
    device = models.ForeignKey(SlaveDevice, on_delete=models.CASCADE)


class ControlledModule(models.Model):
    name = models.TextField(max_length=120)
    module_code = models.IntegerField()
    device = models.ForeignKey(SlaveDevice, on_delete=models.CASCADE)


class SlaveDeviceAlg(models.Model):
    name = models.TextField(max_length=120)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    module = models.ForeignKey(ControlledModule, on_delete=models.CASCADE)
    start_value = models.IntegerField()
    stop_value = models.IntegerField()


class Token(models.Model):
    value = models.TextField(max_length=8)
    device = models.ForeignKey(MainDevice, on_delete=models.CASCADE)


class SensorsData(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.IntegerField()

