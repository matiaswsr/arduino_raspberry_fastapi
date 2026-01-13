from fastapi import APIRouter, HTTPException
from app.services.serial_service import serial_service

router = APIRouter(prefix="/led", tags=["LED"])

@router.post("/on")
def led_on():
    response = serial_service.send_command("LED_ON")
    if response != "OK":
        raise HTTPException(status_code=500, detail="Arduino error")
    return {"status": "on"}

@router.post("/off")
def led_off():
    response = serial_service.send_command("LED_OFF")
    if response != "OK":
        raise HTTPException(status_code=500, detail="Arduino error")
    return {"status": "off"}
