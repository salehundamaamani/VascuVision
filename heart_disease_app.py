# -*- coding: utf-8 -*-

import numpy as np
import pickle
from flask import Flask, request, render_template

# Load ML model
model = pickle.load(open('model.pkl', 'rb')) 

# Create application
app = Flask(__name__, static_url_path='/static')




# Custom home page
@app.route('/')
def vascuvision():
    return render_template('Vascuvision_home.html')

@app.route('/file_upload')
def file_upload():
    return render_template('file_upload.html')

@app.route('/file_uploaded_sucess')
def file_upload_sucess():
    return render_template('file_uploaded_sucess.html')

# Bind home function to URL
@app.route('/Heart_disease_classifier')
def Heart_disease_classifier():
    return render_template('Heart_disease_classifier.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)
    
    output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template('Heart_disease_classifier.html', 
                               result1 = 'Based on the input parameters, the patient is not likely to have heart disease!')
    else:
        return render_template('Heart_disease_classifier.html', 
                               result2 = 'Based on the input parameters, The patient is likely to have heart disease!')

if __name__ == '__main__':
#Run the application
    app.run()
    
    