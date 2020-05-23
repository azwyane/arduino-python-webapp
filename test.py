import requests
from collections import deque
import time 
import json
#import winsound

delay=5 #delay applied considering requests delay 
frequency = 2500  # 2500 Hertz
duration = 3000   # 3 sec

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
            
    celsius_tempt_bytes= input(">")  #edit here as per arguments
    celsius_tempt = celsius_tempt_bytes
    if celsius_tempt: 
        Day,Time = time.strftime('%d/%m/%Y'),time.strftime('%H:%M:%S')
        data_to_push.append({"Day":Day,"Time":Time,"Tempt":celsius_tempt})                   # here also
        push_arduino_data_to_database()
        if (20 <= int(celsius_tempt) and int(Day[3:-5]) <= 7) or (15 <= int(celsius_tempt) and int(Day[3:-5]) > 7):
            #winsound.Beep(frequency, duration)
            print("beep")
        time.sleep(delay)
    
  except IOError:
    print('Got some IO error')
  
  

