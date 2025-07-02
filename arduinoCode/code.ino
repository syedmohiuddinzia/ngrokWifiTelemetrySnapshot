#include <SoftwareSerial.h>

const int buttonPin = 2;     // Pin where button is connected
const int rxPin = 10;        // SoftwareSerial RX pin (not used here, but required)
const int txPin = 11;        // SoftwareSerial TX pin

SoftwareSerial mySerial(rxPin, txPin); // RX, TX

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);  // Use internal pull-up resistor
  Serial.begin(115200);              // Hardware serial to PC
  mySerial.begin(57600);              // Software serial (you can change baud rate)
}

void loop() {
  static bool lastButtonState = HIGH;
  bool buttonState = digitalRead(buttonPin);

  // Button press detection (active low)
  if (lastButtonState == HIGH && buttonState == LOW) {
    Serial.println('c');    // Send to hardware serial (PC)
    mySerial.println('c');  // Send to software serial device
    delay(200);             // Debounce delay
  }
  lastButtonState = buttonState;
}
