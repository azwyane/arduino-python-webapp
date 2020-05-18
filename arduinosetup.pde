float tempt,humid,pressur; 
int temppin = 0;
int humidpin = 1;
int pressur = 2;
void setup() {            //This function gets called when the Arduino starts
  Serial.begin(9600);   //This code sets up the Serial port at 9600 baud rate
}
 
void loop() {             //This function loops while the arduino is powered
                 //Create an integer variable
  tempt=analogRead(0)*0.48828125;      //Read the analog port 0 where temperature sensor is connected and store the value in tempt
  humid=analogRead(1);     //Read humidity from port 1
  pressur=analogRead(2);
  Serial.println(tempt);    //Print the temperature value to the serial port  Serial.println(humid);
  Serial.println(humid);
  Serial.println(pressur);
  delay(30000);            //Wait 30 second before we do it again
}




