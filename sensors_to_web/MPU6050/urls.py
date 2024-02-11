# urls.py
from django.urls import path
from MPU6050 import motion_detect_view,basic_view

urlpatterns = [
    path('basic_data/', basic_view.serial_data_view , name='basic_data'),
    path('basic_plot/',basic_view.basic_template.as_view() , name='basic_plot'),

    path('motion_data/',motion_detect_view.MotionDetectView.as_view() , name='motion_data'),
    path('motion_plot/', motion_detect_view.MotionDetectView.as_view(), name='motion_plot'),
]
