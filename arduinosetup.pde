#define tempPin A0

int tempt;
void setup() {            //arduino setup for ports
  Serial.begin(9600);   //set up the Serial port at 9600 baud rate
}
 
void loop() {             //arduino loops the functionality when powered on
               
  tempt=analogRead(tempPin);      //Read the analog port 0 where temperature sensor is connected and store the value in tempt
  float temptCel=tempt*0.48828125;  //Convert into degree celcius
  Serial.println(temptCel);    //Print the temperature value to the serial port  
  delay(30000);            //Wait 30 second before it loops again
}




