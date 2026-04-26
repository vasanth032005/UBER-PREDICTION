import numpy as np 
from flask import Flask,render_template,request
import math 
import pickle

app=Flask(__name__)

model2=pickle.load(open("model.pkl","rb")) 

@app.route("/")
def home():
    return render_template('index.html')

import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    final_features = np.array([[
        float(request.form['Priceperweek']),
        float(request.form['Population']),
        float(request.form['Monthlyincome']),
        float(request.form['Averageparkingpermonth']),
        float(request.form['Numberofcars'])
    ]])
    
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('index.html',
                           prediction_text=f'Predicted Weekly Riders: {output}')


if __name__ == '__main__':
    app.run(debug=True)