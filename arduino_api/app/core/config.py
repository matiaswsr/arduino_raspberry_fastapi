import os

SERIAL_PORT = os.getenv("ARDUINO_SERIAL_PORT", "/dev/ttyACM0")
SERIAL_BAUDRATE = int(os.getenv("ARDUINO_BAUDRATE", "9600"))
SERIAL_TIMEOUT = float(os.getenv("ARDUINO_TIMEOUT", "2"))




