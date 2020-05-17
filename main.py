from flask import Flask,render_template
from flask_restful import Resource, Api
#import requests
import pandas as pd


app=Flask(__name__)
api=Api(app)

# change this url to the sheet csv url
sheet_url="https://docs.google.com/spreadsheets/d/e/2PACX-1vQujRCxtaNiPA3VT_CPtdeydwKj4sylSNCpRLIoWWijco_QN-pL0GbD9A9MT-W-g-qRO-8vpcWEN2zF/pub?gid=0&single=true&output=csv"    
 
def read_sheets_api():
    df=pd.read_csv(sheet_url)
    row_data=[[val for key,val in dict(df.loc[x]).items()] for x in range(len(df))]
    api_format=[]
    for row_index in range(len(row_data)):
        pre_msg=dict([(column_name,row_values) for column_name,row_values in zip(["time","temperature","humidity","pressure"],row_data[row_index])]) #remove pressure if you dont have that field
        api_format.append(pre_msg)
    return api_format
     
class data_api(Resource):
    def get(self):
        
        return read_sheets_api()

api.add_resource(data_api, '/api/data/')

def read_sheets_notification():
    '''
    This function updates the latest index value from
    the sheets.
    '''
    df=pd.read_csv(sheet_url)
    with open('lastrowindex.txt','r+',encoding = 'utf-8') as f:
   
        read_index=int(f.read())
        if len(df)>read_index:
            f.seek(0)
            f.write(str(len(df)))
            f.truncate()
            return str(df.iloc[read_index:len(df), : ])
        else:
            return "No new data"
            

@app.route("/")
def home():
   
    #return render_template("home.html",name="hey")
    return read_sheets_notification()
    
@app.route("/datarecorded")
def data_recorded():
    return render_template("datarecorded.html")
    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404    
    
if __name__=="__main__":
    app.run(debug=True)


