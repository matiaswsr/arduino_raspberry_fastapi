#include <DHT.h>

#define LED_PIN     8
#define DHT_PIN     7
#define DHT_TYPE    DHT11
#define TRIG_PIN    5
#define ECHO_PIN    6

DHT dht(DHT_PIN, DHT_TYPE);

String command = "";

void setup() {
  Serial.begin(9600);

  pinMode(LED_PIN, OUTPUT);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  digitalWrite(LED_PIN, LOW);
  digitalWrite(TRIG_PIN, LOW);

  dht.begin();

  Serial.println("READY");
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();

    if (c == '\n') {
      processCommand(command);
      command = "";
    } else if (c != '\r') {
      command += c;
    }
  }
}

void processCommand(String cmd) {
  cmd.trim();
  if (cmd == "LED_ON") {
    digitalWrite(LED_PIN, HIGH);
    Serial.println("OK");
  }else if (cmd == "LED_OFF") {
    digitalWrite(LED_PIN, LOW);
    Serial.println("OK");
  }else if (cmd == "READ_DHT") {
    readDHT();
  }else if (cmd == "READ_DIST") {
    readDistance();
  }else {
    Serial.println("ERROR");
  }
}

void readDHT() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("ERROR");
    return;
  }

  Serial.print("TEMP:");
  Serial.print(t);
  Serial.print(",HUM:");
  Serial.println(h);
}

void readDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long dur = pulseIn(ECHO_PIN, HIGH, 30000);
  if (dur == 0) {
    Serial.println("ERROR");
    return;
  }

  float dist = dur * 0.0343 / 2;
  Serial.print("DIST:");
  Serial.println(dist);
}
