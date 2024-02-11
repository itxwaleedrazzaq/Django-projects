from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import serial
from django.views.generic import TemplateView

class basic_template(TemplateView):
    template_name = 'MPU6050/basic_data.html'

@csrf_exempt  
def serial_data_view(request):
    ser = serial.Serial('/dev/ttyACM0', baudrate=115200)
    serial_output = ser.readline().decode('utf-8').strip()
    data_parts = serial_output.split(',')

    acceleration_x, acceleration_y, acceleration_z = 0, 0, 0
    rotation_x, rotation_y, rotation_z = 0, 0, 0
    temperature = 0

    for part in data_parts:
        key_value = part.split(':')
        if len(key_value) == 2:
            if "Acceleration X" in key_value[0]:
                acceleration_x = float(key_value[1])
            elif "Y" in key_value[0]:
                acceleration_y = float(key_value[1])
            elif "Z" in key_value[0]:
                acceleration_z = float(key_value[1])
            elif "Rotation X" in key_value[0]:
                rotation_x = float(key_value[1])
            elif "Y" in key_value[0]:
                rotation_y = float(key_value[1])
            elif "Z" in key_value[0]:
                rotation_z = float(key_value[1])
            elif "Temperature" in key_value[0]:
                temperature = float(key_value[1])

    data_dict = {
        "acceleration_x": acceleration_x,
        "acceleration_y": acceleration_y,
        "acceleration_z": acceleration_z,
        "rotation_x": rotation_x,
        "rotation_y": rotation_y,
        "rotation_z": rotation_z,
        "temperature": temperature,
    }
    ser.close()
    return JsonResponse(data_dict)

