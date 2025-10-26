#include <WiFiS3.h>

// ====== CONFIG ======
const char* ssid     = "wifi_ssid";
const char* password = "password";
// ====================

void setup() {
  // Start Serial but DON'T block forever if it's not open yet.
  Serial.begin(9600);
  unsigned long start = millis();
  while (!Serial && (millis() - start < 3000)) {
    ; // wait up to 3s for Serial Monitor to attach
  }

  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  Serial.println("\n[UNO R4 WiFi] Booting...");
  delay(100);

  // Optional: print WiFi firmware version of the ESP32-S3 coprocessor
  Serial.print("WiFi firmware: ");
  Serial.println(WiFi.firmwareVersion());

  Serial.print("Connecting to SSID: ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  // Progress dots so you can see it's alive even if baud is wrong
  int dots = 0;
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print('.');
    if (++dots % 10 == 0) Serial.println();
    // Blink to show the sketch is running
    digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
  }

  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("\nConnected!");
  Serial.print("IP address: ");   Serial.println(WiFi.localIP());
  Serial.print("RSSI (dBm): ");   Serial.println(WiFi.RSSI());
  uint8_t mac[6];
  WiFi.macAddress(mac);

  Serial.print("MAC: ");
  for (int i = 0; i < 6; i++) {
    if (mac[i] < 16) Serial.print('0'); // leading zero for single hex digits
      Serial.print(mac[i], HEX);
        if (i < 5) Serial.print(':');
    }
  Serial.println();

}

void loop() {
  // Keep-alive print every 5s so you know Serial is working
  static unsigned long t0 = 0;
  if (millis() - t0 > 5000) {
    t0 = millis();
    Serial.print("[WiFi] Status: "); Serial.println(WiFi.status());
    Serial.println(WiFi.localIP());  Serial.println(WiFi.RSSI());
  }
}
