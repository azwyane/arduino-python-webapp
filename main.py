from flask import Flask,render_template
from flask_restful import Resource, Api
import requests 
import json

app=Flask(__name__)
api=Api(app)

# change this url to your firebase url
database_url="https://arduino-36d7e.firebaseio.com"    

def read_sheets_api():
    '''
    This function makes get request to the firebase
    in a json format.
    '''
    get_data_from_database=requests.get(database_url+"/arduinodata.json")
    data_into_dict=get_data_from_database.json()
    api_format=[values for keys,values in data_into_dict.items()]
    return api_format[::-1]
     
class data_api(Resource):
    def get(self):
        return read_sheets_api()
        
         
api.add_resource(data_api,'/api/data/')

def read_sheets_notification():
    '''
    This function updates the latest index value from
    the sheets.
    '''
    get_data_from_database=requests.get(database_url+"/arduinodata.json")
    data_into_dict=get_data_from_database.json()
    refined_data=[values for keys,values in data_into_dict.items()]
    with open('lastrowindex.txt','r+',encoding = 'utf-8') as f:
   
        read_index=int(f.read())
        if read_index<len(data_into_dict):
            f.seek(0)
            f.write(str(len(data_into_dict)))
            f.truncate()
            return refined_data[read_index:len(data_into_dict)]
        else:
            return []
            

@app.route("/")
def home():
    '''
    It is the home of the webapp
    where user can see the unseen and unverified data.
    '''
    new_data=read_sheets_notification()
    return render_template("home.html",new_data=newdata)
   
    
@app.route("/datarecorded")
def data_recorded():
    '''
    It is the data store display function which 
    display all data pushed from arduino which is 
    saved in the database.
    '''
    total_data_in=read_sheets_api()
    return render_template("datarecorded.html",api=total_data_in)
    
@app.errorhandler(404)
def page_not_found(error):
    '''
    Error function
    '''
    return render_template('page_not_found.html'), 404    
    
if __name__=="__main__":
    '''
    While deploying into the main server
    this may not be required.
    '''
    app.run(debug=True)  #set to False when deploying


