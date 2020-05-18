import requests
import serial
from collections import deque
from time import sleep

delay=30

global tempt,humid,pressure
URL="https://script.google.com/macros/s/AKfycby8GpFlvX-EWcuwlbONVZVcq0C1ZW80chRC7UdCZO0XG6Db4hXU/exec?"
data_to_push=deque([])
#ser = serial.Serial('/dev/ttyUSB0') #can also be '/dev/ttyACM0' check your arduino serial port address
#ser = serial.Serial('COM15', 9600, timeout=0)


def push_arduino_data_to_sheets():
    while data_to_push:
        data=data_to_push.popleft()
        URL_with_data=URL+f'temperature={data["tempt"]}&humidity={data["humid"]}&pressure={data["pressure"]}'
        res=requests.get(URL_with_data)
        if (res.status_code==200):
            print("Data pushed successfully")
        else:
            print("Failed to push data")
            
            
            
            
while 1:
  try:
            
    tempt,humid,pressure = ser.readline()   #edit here as per arguments
    data_to_push.append({"tempt":tempt,"humid":humid,"pressure":pressure})                   # here also
    push_arduino_data_to_sheets()
    sleep(delay)
  except IOError:
    print('Got some error')
  sleep(delay)



#def get_arduino_data_from_usb():
#    data_to_push.append()
#    pass





#
#make this all separately run
#keep data into a list of dict with tempt,... 
#loop to pop items in that same list until the list is empty
#


