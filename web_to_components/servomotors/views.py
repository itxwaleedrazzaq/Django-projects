import serial
from django.shortcuts import render

# view for catching angle from html form
ser = serial.Serial('/dev/ttyACM0',9600)
def pan_tilt_angle(request):
    if request.method == 'POST':
        pan_angle = request.POST.get('pan_angle')
        tilt_angle = request.POST.get('tilt_angle')
        print(pan_angle)
        print(tilt_angle)
        if pan_angle is not None and tilt_angle is not None:
            # Assuming ser is a valid Serial object
            pan_angle_bytes = bytes(str(pan_angle), 'utf-8')
            tilt_angle_bytes = bytes(str(tilt_angle), 'utf-8')

            # Ensure a consistent length for each value (adjust as needed)
            pan_angle_bytes = pan_angle_bytes.ljust(8, b'\0')
            tilt_angle_bytes = tilt_angle_bytes.ljust(8, b'\0')

            ser.write(pan_angle_bytes)
            ser.write(tilt_angle_bytes)

        else:
            print('SOME ERROR')

    return render(request,'servomotors/servo.html',{})
