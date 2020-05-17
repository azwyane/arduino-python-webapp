from flask import Flask,render_template
from flask_restful import Resource, Api
#import requests
import pandas as pd

app=Flask(__name__)
api=Api(app)

# change this url to the sheet csv url
sheet_url="https://docs.google.com/spreadsheets/d/e/2PACX-1vQujRCxtaNiPA3VT_CPtdeydwKj4sylSNCpRLIoWWijco_QN-pL0GbD9A9MT-W-g-qRO-8vpcWEN2zF/pub?gid=0&single=true&output=csv"    
 
def read_sheets():
    df=pd.read_csv(sheet_url)
    row_data=[[df.loc[x]] for x in range(len(df))]
    api_format=dict(list((column_name,row_values) for column_name,row_values in zip(["time","temperature","humidity","pressure"],row_data)))
    return df.loc[0]
     
class data_api(Resource):
    def get(self):
        
        return read_sheets()

api.add_resource(data_api, '/api/data/')

@app.route("/")
def home():
   
    #return render_template("home.html",name="hey")
    return str(read_sheets())
    
@app.route("/datarecored")
def data_recorded():
    return render_template("datarecorded.html",name=None)
if __name__=="__main__":
    app.run(debug=True)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
