const int trigPin = 2;
const int echoPin = 3;
const double pipeLength = 36.5; 

void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  static int count = 0;

  // if (count >= 100) { 
  //   return;
  // }

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);

  double speedOfSound = (pipeLength * 2 / 100) / (duration / 1e6);

  
  Serial.print("Speed of Sound: ");
  Serial.println(speedOfSound);
  //Serial.println(" m/s");
  count++;


  delay(1000);
}
