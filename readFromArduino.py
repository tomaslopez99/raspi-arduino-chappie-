import serial

ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

while 1:
    while ser.in_waiting:
        print ser.read()
