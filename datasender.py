import requests
import serial
from collections import deque
import time 
import json
import winsound

# email service
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

delay=25 #delay applied considering requests delay 
frequency = 2500  # 2500 Hertz
duration = 3000   # 3 sec
critical_tempt_count = 0 #send email in particular interval

URL="https://arduino-36d7e.firebaseio.com"
#URL="https://arduino-c666e.firebaseio.com"   

data_to_push=deque([]) #made a deque object for future extension to run request independently
#ser = serial.Serial('/dev/ttyUSB0',9600,timeout=0) #can also be '/dev/ttyACM0' check your arduino serial port address
ser = serial.Serial('COM7', 9600, timeout=0)
ser.flushInput()

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
            
    celsius_tempt_bytes= ser.readline()    #edit here as per arguments
    celsius_tempt = celsius_tempt_bytes[0:-2].decode("utf-8")
    if celsius_tempt: 
        Day,Time = time.strftime('%d/%m/%Y'),time.strftime('%H:%M:%S')
        data_to_push.append({"Day":Day,"Time":Time,"Tempt":celsius_tempt})                   # here also
        push_arduino_data_to_database()
        if (20 <= float(celsius_tempt) and int(Day[3:-5]) <= 7) or (15 <= float(celsius_tempt) and int(Day[3:-5]) > 7):
            winsound.Beep(frequency, duration)
            critical_tempt_count+=1

            if (critical_tempt_count % 4 == 0):      #send email in every delay*4 sec
                # send email about critical temperature 
                message = Mail(
                    from_email = '<your_email>',
                    to_emails = ['<receipient_email>',],
                    subject='Critical Temperature Alert',
                    html_content=f'''
                    <strong>Arduino Temperature Alert</strong>
                    <ul>
                    <li>DAY: {Day}</li>
                    <li>TIME: {Time}</li>
                    <li>TEMPERATURE: {celsius_tempt}</li>
                    </ul>
                    '''
                    )

                SendGridAPIClient("<your_api_key>").send(message)

        else:
            critical_tempt_count = 0

        time.sleep(delay)
    
  except IOError:
    print('Got some IO error')
  






