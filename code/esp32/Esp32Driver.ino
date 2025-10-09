#include <WiFi.h>
#include <HTTPClient.h>
#include "env.h"

#define UART_RX_PIN 16  // RX dell'ESP32 collegato a TX dello STM32
#define UART_TX_PIN 17  // TX dell'ESP32 (opzionale)

void setup() {
  Serial.begin(115200);  // Per debug
  
  // ✅ Configura Serial2 (UART2) con i tuoi pin
  Serial2.begin(115200, SERIAL_8N1, UART_RX_PIN, UART_TX_PIN);
  Serial2.setTimeout(100);
  
  WiFi.begin(ssid, password);
  Serial.println("Connecting...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected!");
  Serial.println(WiFi.localIP());
  
  Serial.println("UART pronto, in attesa dati...");
}

void loop() {
  if (Serial2.available()) {
    uint8_t rx_byte = Serial2.read();
    
    Serial.printf("Ricevuto: %d\n", rx_byte);
      
      if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        WiFiClient client;
        http.begin(client, serverName);
        http.addHeader("Content-Type", "application/json");

        String json = "{\"umidita\": \"" + String(rx_byte) + "\"}";
        int code = http.POST(json);

        Serial.printf("Inviato -> %s | Response: %d\n", json.c_str(), code);
        http.end();
      }

  delay(10);
  }
}