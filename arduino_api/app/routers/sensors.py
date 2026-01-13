from fastapi import APIRouter, HTTPException
from app.services.serial_service import serial_service

router = APIRouter(prefix="/sensores", tags=["Sensores"])

@router.get("/dht11")
def read_dht():
    response = serial_service.send_command("READ_DHT")
    if not response.startswith("TEMP"):
        raise HTTPException(status_code=500, detail="Arduino error")
    temp, hum = response.replace("TEMP:", "").split(",HUM:")
    return {
        "temperatura": float(temp),
        "humedad": float(hum)
    }


@router.get("/distancia")
def read_distance():
    response = serial_service.send_command("READ_DIST")
    if not response.startswith("DIST"):
        raise HTTPException(status_code=500, detail="Arduino error")
    return {
        "distancia_cm": float(response.replace("DIST:", ""))
    }
