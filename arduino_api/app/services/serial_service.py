import serial
import time
from app.core.config import SERIAL_PORT, SERIAL_BAUDRATE, SERIAL_TIMEOUT

class SerialService:
    def __init__(self):
        self._serial = serial.Serial(
            port=SERIAL_PORT,
            baudrate=SERIAL_BAUDRATE,
            timeout=SERIAL_TIMEOUT
        )
        time.sleep(2)  # estabilización Arduino, 2 segundos

    def send_command(self, command: str) -> str:
        self._serial.reset_input_buffer()
        self._serial.write(f"{command}\n".encode())
        response = self._serial.readline().decode().strip()
        return response

    def close(self):
        if self._serial.is_open:
            self._serial.close()

serial_service = SerialService()
