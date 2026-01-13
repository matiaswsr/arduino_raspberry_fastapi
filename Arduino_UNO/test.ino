#include <DHT.h>

#define LED_PIN     8
#define DHT_PIN     7
#define DHT_TYPE    DHT11
#define TRIG_PIN    5
#define ECHO_PIN    6

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
  Serial.begin(9600);
  while (!Serial); // asegura conexión estable

  pinMode(LED_PIN, OUTPUT);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  digitalWrite(LED_PIN, LOW);
  digitalWrite(TRIG_PIN, LOW);

  dht.begin();

  Serial.println("=== INICIO TEST HARDWARE ===");
}

void loop() {
  testLED();
  testDHT11();
  testUltrasonico();

  Serial.println("-----------------------------");
  delay(3000);
}

void testLED() {
  Serial.println("LED: ENCENDIENDO");
  digitalWrite(LED_PIN, HIGH);
  delay(500);

  Serial.println("LED: APAGANDO");
  digitalWrite(LED_PIN, LOW);
  delay(500);
}

void testDHT11() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("DHT11: ERROR DE LECTURA");
    return;
  }

  Serial.print("DHT11: Humedad = ");
  Serial.print(h);
  Serial.print(" % | Temperatura = ");
  Serial.print(t);
  Serial.println(" C");
}

void testUltrasonico() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duracion = pulseIn(ECHO_PIN, HIGH, 30000); // timeout 30 ms

  if (duracion == 0) {
    Serial.println("HC-SR04: SIN ECO");
    return;
  }

  float distancia = duracion * 0.0343 / 2;

  Serial.print("HC-SR04: Distancia = ");
  Serial.print(distancia);
  Serial.println(" cm");
}

