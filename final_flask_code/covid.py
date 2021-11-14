from flask import Flask
from flask import render_template, request

app = Flask(__name__)



@app.route("/")
def data_input():
    return render_template('./index.html', title='Home')  

@app.route("/output", methods=['POST',])
def data_output():
    percentage = "25"
    import machine_learning as ml
    #result =  ml.result()
    if request.form['Breathing Problem'] == 'nai':
        feature1 = 1
    elif request.form['Breathing Problem'] == 'oxi':
        feature1 = 0
    if request.form['fever'] == 'nai':
        feature2 = 1
    elif request.form['fever'] == 'oxi':
        feature2 = 0
    if request.form['Dry Cough'] == 'nai':
        feature3 = 1
    elif request.form['Dry Cough'] == 'oxi':
        feature3 = 0
    if request.form['Headache'] == 'nai':
        feature4 = 1
    elif request.form['Headache'] == 'oxi':
        feature4 = 0
    if request.form['Contact with COVID Patient'] == 'nai':
        feature5 = 1
    elif request.form['Contact with COVID Patient'] == 'oxi':
        feature5 = 0
    if request.form['Family working in Public Exposed Places'] == 'nai':
        feature6 = 1
    elif request.form['Family working in Public Exposed Places'] == 'oxi':
        feature6 = 0
    if request.form['Wearing Masks'] == 'nai':
        feature7 = 1
    elif request.form['Wearing Masks'] == 'oxi':
        feature7 = 0
    import numpy as np
    myfeatures = np.array([[feature1,feature2,feature3,feature4,feature5,feature6,feature7],
                ])        
    result2 = ml.result2(myfeatures)[0][1]
    return render_template('output.html', title='Output', result2 = result2)  

app.run(host='0.0.0.0', port=81)
