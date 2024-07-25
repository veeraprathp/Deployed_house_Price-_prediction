from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


Application = Flask(__name__)
app = Application

#import the Multiple Linear Regrssion pickle

Regressor_model = pickle.load(open("models1/regressor.pkl",'rb'))
Standard_scaler = pickle.load(open("models1/scaler.pickle",'rb'))


@app.route("/")
def index():
    return render_template('index.html')
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route('/predictata',methods =['GET','POST'])
def predict_datapoint():
    if request.method =='POST':
       MedInc = float(request.form.get('MedInc'))
       HouseAge = float(request.form.get('HouseAge'))
       AveRooms = float(request.form.get('AveRooms'))
       Population = float(request.form.get('Population'))
       AveOccup = float(request.form.get('AveOccup'))
       Latitude = float(request.form.get('MedInc'))
       Longitude = float(request.form.get('Longitude'))

       input_data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])

       new_scaled_data=scaler.transform([[MedInc,HouseAge,AveRooms,AveBedrms,Population	,AveOccup,Latitude,Longitude]])
       reslut= regressor.predict(new_scaled_data)
    else:
        return render_template('Home.html',resluts = [0])

if __name__=="__main__":
    app.run(host="0.0.0.0")
