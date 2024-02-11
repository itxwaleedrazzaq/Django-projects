import serial
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

serial_port = '/dev/ttyACM0' 
baud_rate = 115200
ser = serial.Serial(serial_port, baud_rate)

class Template(TemplateView):
    template_name = 'MPU6050/motion_html.html'

class MotionDetectView(View):
    def get(self, request, *args, **kwargs):
        data = {
                    'accel_x': 0,
                    'accel_y': 0,
                    'accel_z': 0,
                    'gyro_x': 0,
                    'gyro_y': 0,
                    'gyro_z': 0,
                }
        line = ser.readline().decode('utf-8').strip()
        if "AccelX" in line and "AccelY" in line and "AccelZ" in line and "GyroX" in line and "GyroY" in line and "GyroZ" in line:
            values = line.split(',')

            accel_x = float(values[0].split(':')[1])
            accel_y = float(values[1].split(':')[1])
            accel_z = float(values[2].split(':')[1])
            gyro_x = float(values[3].split(':')[1])
            gyro_y = float(values[4].split(':')[1])
            gyro_z = float(values[5].split(':')[1])

            data = {
                'accel_x': accel_x,
                'accel_y': accel_y,
                'accel_z': accel_z,
                'gyro_x': gyro_x,
                'gyro_y': gyro_y,
                'gyro_z': gyro_z,
            }
            return JsonResponse(data)
        return JsonResponse(data)
