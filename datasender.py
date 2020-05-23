import requests
import serial
from collections import deque
import time 
import json
import winsound

delay=30 #delay applied considering requests delay 
frequency = 2500  # 2500 Hertz
duration = 3000   # 3 sec

URL="https://arduino-36d7e.firebaseio.com"
#URL="https://arduino-c666e.firebaseio.com"   

data_to_push=deque([]) #made a deque object for future extension to run request independently
#ser = serial.Serial('/dev/ttyUSB0',9600,timeout=0) #can also be '/dev/ttyACM0' check your arduino serial port address
ser = serial.Serial('COM7', 9600, timeout=0)
ser.flushInput()

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
            
    celsius_tempt_bytes= ser.readline()    #edit here as per arguments
    celsius_tempt = celsius_tempt_bytes[0:-2].decode("utf-8")
    if celsius_tempt: 
        Day,Time = time.strftime('%d/%m/%Y'),time.strftime('%H:%M:%S')
        data_to_push.append({"Day":Day,"Time":Time,"Tempt":celsius_tempt})                   # here also
        push_arduino_data_to_database()
        if (20 <= celsius_tempt and Day[3:-5] <= 7) or (15 <= celsius_tempt and Day[3:-5] > 7):
            winsound.Beep(frequency, duration)
        time.sleep(delay)
    
  except IOError:
    print('Got some IO error')
  
  time.sleep(delay)





