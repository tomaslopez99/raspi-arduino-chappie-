import serial

arduinoSerialData = serial.Serial('/dev/cu.usbmodem1411', 9600)
arduinoSerialData.write('5')
