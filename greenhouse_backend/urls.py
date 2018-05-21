from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/login/', obtain_auth_token),
    path('api/device/', include('device.urls')),
]
