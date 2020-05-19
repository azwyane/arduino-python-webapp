import requests
from collections import deque
import time 
import json

delay=5 #same delay applied to arduino

URL="https://arduino-36d7e.firebaseio.com/"

data_to_push=deque([])

def push_arduino_data_to_database():
    while data_to_push:
        data=data_to_push.popleft()
        res=requests.post(URL+"/arduinodata.json", data=json.dumps(data))
        if (res.status_code==200):
            print("Data pushed successfully")
        else:
            print("Failed to push data")
            
            
            
            
while True:
  try:
            
    celcius_tempt= input(">")  #edit here as per arguments
    data_to_push.append({"Day":time.strftime('%d/%m/%Y'),"Time":time.strftime('%H:%M:%S'),"Tempt":celcius_tempt})                   # here also
    push_arduino_data_to_database()
    time.sleep(delay)
    
  except IOError:
    print('Got some IO error')
  
  time.sleep(delay)

