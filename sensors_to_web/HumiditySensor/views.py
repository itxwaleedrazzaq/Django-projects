from django.http import JsonResponse
import serial
from django.views.generic import TemplateView

ser = serial.Serial('/dev/ttyACM0', 9600)

def parse_data(data):
    parts = data.split(',')
    sensor_data = {}

    for part in parts:
        if ':' in part:
            key, value = part.split(':')
            sensor_data[key.strip()] = float(value.strip())
    return sensor_data

def sensor_data(request):
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        sensor_data = parse_data(line)
        return JsonResponse(sensor_data)
    else:
        return JsonResponse({"error": "No data available"}, status=404)

class Humidity_plot(TemplateView):
    template_name = 'HumiditySensor/humidity_plot.html'