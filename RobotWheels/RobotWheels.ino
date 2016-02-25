#include <AFMotor.h>
AF_DCMotor motorM3(3, MOTOR12_64KHZ); // create motor #3, 64KHz pwm
AF_DCMotor motorM2(2, MOTOR12_64KHZ); // create motor #3, 64KHz pwm
void setup() {
Serial.begin(9600); // set up Serial library at 9600 bps
Serial.println("Motor test!");
motorM3.setSpeed(255); // set the speed to 200/255
motorM2.setSpeed(255); // set the speed to 200/255
}
void loop() {
Serial.print("tick");
motorM3.run(FORWARD); // turn it on going forward
motorM2.run(FORWARD); // turn it on going forward
delay(1000);
Serial.print("tock");
motorM3.run(BACKWARD); // the other way
motorM2.run(BACKWARD); // the other way
delay(1000);
Serial.print("tack");
motorM3.run(RELEASE); // stopped
motorM2.run(RELEASE); // stopped
delay(1000);
}
