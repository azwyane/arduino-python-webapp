import requests
from collections import deque
import time 
import json
#import winsound
import os

# email service
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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
        if (20 <= float(celsius_tempt) and int(Day[3:-5]) <= 7) or (15 <= float(celsius_tempt) and int(Day[3:-5]) > 7):
            #winsound.Beep(frequency, duration)
            print("beep")
             # send email about critical temperature
            message = Mail(
                    from_email = '<your_email>',
                    to_emails = ['<recipient_email>',],
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
            
        time.sleep(delay)
    
  except IOError:
    print('Got some IO error')
  
  

