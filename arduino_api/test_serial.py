import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)
time.sleep(2)

ser.write(b'LED_ON\n')
print(ser.readline().decode().strip())

ser.write(b'READ_DHT\n')
print(ser.readline().decode().strip())

ser.write(b'READ_DIST\n')
print(ser.readline().decode().strip())

ser.write(b'LED_OFF\n')
print(ser.readline().decode().strip())

ser.close()
