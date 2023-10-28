from flask import Flask, request, render_template, url_for
import pickle
import numpy as np
import json
import requests



app = Flask(__name__)
with open('model.pkl', 'wb') as file:
    model = pickle.load(file)

@app.route("/")
def f():
    return render_template("index.html")

@app.route("/inspect")
def inspect():
    return render_template("inspect.html")


@app.route("/output", methods=["GET", "POST"])
def output():
    if request.method == 'POST':
        var1 = request.form["ph"]
        var2 = request.form["Hardness"]
        var3 = request.form["Solids"]
        var4 = request.form["Chloramines"]
        var5 = request.form["sulfate"]
        var6 = request.form["Conductivity"]
        var7 = request.form["Organic_carbon"]
        var8 = request.form["Trihalomethanes"]
        var9 = request.form["Turbidity"]
        var10 = request.form["Potability"]
     

        # Convert the input data into a numpy array
        predict_data = np.array([var1, var2, var3, var4, var5, var6, var7, var8, var9, var10]).reshape(1, -1)

        # Use the loaded model to make predictions
        predict = model.predict(predict_data)

    return render_template("output.html")

if __name__ == "__main__":
    app.run(debug=False)
