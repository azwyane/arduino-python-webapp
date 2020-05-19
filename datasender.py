import requests
import serial
from collections import deque
import time 
import json

delay=27 #delay applied considering requests delay 

URL="https://arduino-36d7e.firebaseio.com"
#URL="https://arduino-c666e.firebaseio.com"   

data_to_push=deque([]) #made a deque object for future extension to run request independently
#ser = serial.Serial('/dev/ttyUSB0',9600,timeout=0) #can also be '/dev/ttyACM0' check your arduino serial port address
ser = serial.Serial('COM15', 9600, timeout=0)


def push_arduino_data_to_database():
    while data_to_push:
        data=data_to_push.popleft()
        res=requests.get(URL+"/arduinodata.json", data=json.dumps(data))
        if (res.status_code==200):
            print("Data pushed successfully")
        else:
            print("Failed to push data")
            
            
            
            
while True:
  try:
            
    celcius_tempt= ser.readline()   #edit here as per arguments
    data_to_push.append({"Day":time.strftime('%d/%m/%Y'),"Time":time.strftime('%H:%M:%S'),"Tempt":celcius_tempt})                   # here also
    push_arduino_data_to_database()
    time.sleep(delay)
    
  except IOError:
    print('Got some IO error')
  
  time.sleep(delay)





