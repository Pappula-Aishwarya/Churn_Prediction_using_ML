import numpy as np
#import pandas as pd
#import sklearn
from flask import Flask, render_template, request

import pickle
#from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open(r'C://Users//YASODHARA//Downloads//churn//churn//models//model.pkl', 'r'))

@app.route('/')
def home():
    return render_template('services.html')

#scaler = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    int_features= [str(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=model.predict(features)
    output=round(prediction[0],2)
    return render_template('services.html',prediction_text='Percent of customer Churn is {}'.format(output))

if __name__=="__main__":
    app.run()