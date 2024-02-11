# urls.py
from django.urls import path
from HumiditySensor import views

urlpatterns = [
    path('humidity_data/', views.sensor_data , name='humidity_data'),
    path('humidity_plot/', views.Humidity_plot.as_view(), name='humidity_plot'),
]
