// ---------------------------------------------------------------------------
// Example NewPing library sketch that does a ping about 20 times per second.
// ---------------------------------------------------------------------------

#include <NewPing.h>
#define LED_PLUS_PIN  10  // Arduino pin tied to Led plus
#define TRIGGER_PIN  12  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN     11  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.

int brightness = 0;    // how bright the LED is
int fadeAmount = 5;    // how many points to fade the LED by

void setup() {
  pinMode(LED_PLUS_PIN, OUTPUT);
  Serial.begin(9600); // Open serial monitor at 115200 baud to see ping results.
}

void loop() {
  delay(50);                      // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
  unsigned int uS = sonar.ping(); // Send ping, get ping time in microseconds (uS).
  Serial.print("Ping: ");
  Serial.print(uS / US_ROUNDTRIP_CM); // Convert ping time to distance and print result (0 = outside set distance range, no ping echo)
  Serial.println("cm");
  
    if(uS / US_ROUNDTRIP_CM < 11){
      analogWrite(LED_PLUS_PIN, 50);
    }else if(uS / US_ROUNDTRIP_CM < 21 & uS / US_ROUNDTRIP_CM > 10){
      analogWrite(LED_PLUS_PIN, 150);
    } else if(uS / US_ROUNDTRIP_CM < 31 & uS / US_ROUNDTRIP_CM > 20){
      analogWrite(LED_PLUS_PIN, 250);
    } else if(uS / US_ROUNDTRIP_CM < 31 & uS / US_ROUNDTRIP_CM > 20){
      analogWrite(LED_PLUS_PIN, 300);
    }else       analogWrite(LED_PLUS_PIN, 10); 
    
  
  
}
