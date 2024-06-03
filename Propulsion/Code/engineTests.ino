volatile int rpmCount = 0;
float rpm = 0;
unsigned long lastTime = 0;

const float a = 0.05;  // Slope from calibration curve
const float b = 1.0;   // Intercept from calibration curve

void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(2), rpmISR, FALLING);
}

void loop() {
  unsigned long currentTime = millis();
  if (currentTime - lastTime >= 1000) {  // Update every second
    noInterrupts();
    rpm = (rpmCount * 60.0) / 1.0;  // Assuming 1 pulse per revolution
    rpmCount = 0;
    lastTime = currentTime;
    interrupts();
    
    // Calculate thrust using the calibration model
    float thrust = a * rpm + b;

    // Print RPM and Thrust value
    Serial.print("RPM: ");
    Serial.print(rpm);
    Serial.print(" | Thrust: ");
    Serial.print(thrust);
    Serial.println(" N");
  }
}

void rpmISR() {
  rpmCount++;
}
