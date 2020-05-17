void setup() {            //This function gets called when the Arduino starts
  Serial.begin(9600);   //This code sets up the Serial port at 9600 baud rate
}
 
void loop() {             //This function loops while the arduino is powered
  int tempt,humid;                //Create an integer variable
  tempt=analogRead(0);      //Read the analog port 0 where temperature sensor is connected and store the value in tempt
  humid=analogRead(1);     //Read humidity from port 1
  Serial.println(tempt);    //Print the temperature value to the serial port  Serial.println(humid);
  delay(30000);            //Wait 30 second before we do it again
}
