import requests
import serial
#import sys



global tempt,humid,pressure
URL="https://script.google.com/macros/s/AKfycby8GpFlvX-EWcuwlbONVZVcq0C1ZW80chRC7UdCZO0XG6Db4hXU/exec?"
data_to_push=[]
ser = serial.Serial('/dev/ttyUSB0') #can also be '/dev/ttyACM0' check your arduino serial port address

def get_arduino_data_from_usb():
    data_to_push.append()
    pass


def push_arduino_data_to_sheets():
    for data in data_to_push:
        URL_with_data=URL+f'temperature={data[tempt]}&humidity={data[humid]}&pressure={data[pressure]}'
    res=requests.get(URL_with_data)
if (res.status_code==200):
    print("Data pushed successfully")
else:
    print("Failed to push data")


#
#make this all separately run
#keep data into a list of dict with tempt,... 
#loop to pop items in that same list until the list is empty
#

if __name__=='__main__':
    p1 = Process(target = get_arduino_data_from_usb)
    p1.start()
    p2 = Process(target = push_arduino_data_to_sheets)
    p2.start()
