from flask import Flask, render_template , request
import numpy as np
import joblib


model = joblib.load('abc.pkl')


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        ph=float(request.form['PH Level'])
        TDS= float(request.form['TDS'])
        Chloride=float(request.form['Chloride'])
        sulfate=float(request.form['Sulfate'])
        Fluoride=float(request.form['Fluoride'])
        TotalHardness=float(request.form['TotalHardness'])

        new_arr=np.array([[ph,TDS,Chloride,sulfate,Fluoride,TotalHardness]])
        new_output = model.predict(new_arr)

        if(new_output[0]==1):
            predicted_result="Water is SAFE to drink !!!"
        else:
            predicted_result="Water is UNSAFE to drink !!!" 
        return render_template('result.html',predicted_result= predicted_result)

    except KeyError as e:
        # Handle missing form fields gracefully
        return "Missing form field: " + str(e), 400
          

if __name__ == "__main__":
    app.run(port=5000,debug=True)