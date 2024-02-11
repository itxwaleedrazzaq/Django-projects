
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('MPU6050/',include('MPU6050.urls')),
    path('HumiditySensor/',include('HumiditySensor.urls'))
]
