const int ledPin = 13;
bool ledState = false;
int fakeButton = 0;

void setup() {
pinMode(ledPin, OUTPUT);
Serial.begin(9600);
}

void loop() {
if (Serial.available() > 0){
  char command = Serial.read();
  if (command == '1') {
    ledState = true;
    Serial.print("LED: ");
    Serial.print(ledState ? "ON" : "OFF");
    Serial.print(" | Button: ");
    Serial.println(fakeButton ? "PRESSED" : "RELEASED");
  } else if (command == '0') {
    ledState = false;
    Serial.print("LED: ");
    Serial.print(ledState ? "ON" : "OFF");
    Serial.print(" | Button: ");
    Serial.println(fakeButton ? "PRESSED" : "RELEASED");
  }
  digitalWrite(ledPin, ledState);
}
// 回傳 LED 狀態和按鈕狀態

delay(500); // 降低 Serial 通訊頻率
}