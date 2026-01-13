const API_BASE = "http://192.168.1.6:8000";

const ledIndicator = document.querySelector("#led-indicator");
const tempSpan = document.querySelector("#temp");
const humSpan = document.querySelector("#hum");
const distSpan = document.querySelector("#dist");

const dhtHistory = document.querySelector("#dht-history");
const distHistory = document.querySelector("#dist-history");

const maxHistory = 5;
function addHistory(list, text) {
    const li = document.createElement("li");
    li.textContent = text;
    list.prepend(li);

    if (list.children.length > maxHistory) {
        list.removeChild(list.lastChild);
    }
}

// LED
document.querySelector("#btn-led-on").addEventListener("click", async () => {
    await fetch(`${API_BASE}/led/on`, { method: "POST" });
    ledIndicator.className = "led-on";
});

document.querySelector("#btn-led-off").addEventListener("click", async () => {
    await fetch(`${API_BASE}/led/off`, { method: "POST" });
    ledIndicator.className = "led-off";
});

// DHT11
document.querySelector("#btn-dht").addEventListener("click", async () => {
    const res = await fetch(`${API_BASE}/sensores/dht11`);
    const data = await res.json();

    tempSpan.textContent = data.temperatura;
    humSpan.textContent = data.humedad;
    addHistory(
        dhtHistory,
        `Temp: ${data.temperatura}°C | Hum: ${data.humedad}%`
    );
});

// DISTANCIA
document.querySelector("#btn-dist").addEventListener("click", async () => {
    const res = await fetch(`${API_BASE}/sensores/distancia`);
    const data = await res.json();
    distSpan.textContent = data.distancia_cm;
    addHistory(
        distHistory,
        `Distancia: ${data.distancia_cm} cm`
    );
});
