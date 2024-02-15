from django.urls import path
from servomotors import views

app_name = 'servomotors'
urlpatterns = [
    path('',views.pan_tilt_angle,name='pan_tilt')
]
