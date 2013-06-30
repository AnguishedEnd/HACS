/*
HACS Arduino 
*/

// pins for the LEDs:
const int led = 13;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // make the pins outputs:
  pinMode(led, OUTPUT); 
}

void loop() {
  if (Serial.available() > 0) {
    if (Serial.peek() == '1') {
      Serial.read();
      digitalWrite(led, HIGH);
    }
    else digitalWrite(led, LOW);
    while (Serial.available() > 0){
      Serial.read();
    }
  }
}










