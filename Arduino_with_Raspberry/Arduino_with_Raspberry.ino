#include <AFMotor.h>

AF_DCMotor motorM2(3, MOTOR12_64KHZ);
AF_DCMotor motorM1(2, MOTOR12_64KHZ);
char receivedChar;
boolean newData = false;

void setup() {

  Serial.begin(9600);

  //pinMode(3, OUTPUT);
  motorM2.setSpeed(255);
  motorM1.setSpeed(255);
  
}

void loop() {

  recvInfo();
  //lightLED();
  moveMotors();
}

void recvInfo() {

  if (Serial.available() > 0) {

    receivedChar = Serial.read();
    Serial.print(receivedChar);
    newData = true;
    
  }
  
}

void lightLED() {

  int led = (receivedChar - '0');

  while(newData == true) {

    digitalWrite(led, HIGH);
    delay(2000);
    digitalWrite(led, LOW);

    newData = false;
    
  }
  
}

void moveMotors() {
  int motorNumber = (receivedChar - '0');
 
  while(newData == true) {
   switch(motorNumber) {
    case 1: Serial.print("Run motor 1");
          motorM1.run(FORWARD);
          delay(1000);
          motorM1.run(RELEASE);
          break;
    case 2: Serial.print("Run motor 2");
          motorM2.run(FORWARD);
          delay(1000);
          motorM2.run(RELEASE);
          break;
    case 3: Serial.print("Run motor 1 and 2");
          motorM2.run(FORWARD);
          motorM1.run(FORWARD);
          delay(1000);
          motorM2.run(RELEASE);
          motorM1.run(RELEASE);
          break;
    case 4: Serial.print("Run motor 1 and 2 backward");
          motorM2.run(BACKWARD);
          motorM1.run(BACKWARD);
          delay(1000);
          motorM2.run(RELEASE);
          motorM1.run(RELEASE);
          break;
   } 
   newData = false;
  }
}
