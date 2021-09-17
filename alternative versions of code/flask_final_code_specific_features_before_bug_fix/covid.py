from flask import Flask
from flask import render_template, request
#?
#from app import app

#?
app = Flask(__name__)

#app.static_folder = 'tmp/static'


@app.route("/")
def data_input():
#    return "<p>Hello, World!</p>"
#    return render_template('index.html', title='Home', user=user)  
    return render_template('./index.html', title='Home')  

@app.route("/output", methods=['POST',])
def data_output():
    #data = request.form
    percentage = "25"
    import machine_learning as ml
    result =  ml.result()
    if request.form['nai Breathing Problem'] == 'on':
        feature1 = 1
    elif request.form['oxi Breathing Problem'] == 'on':
        feature1 = 0
    if request.form['nai fever'] == 'on':
        feature2 = 1
    elif request.form['oxi fever'] == 'on':
        feature2 = 0
    if request.form['nai Dry Cough'] == 'on':
        feature3 = 1
    elif request.form['oxi Dry Cough'] == 'on':
        feature3 = 0
    if request.form['nai Headache'] == 'on':
        feature4 = 1
    elif request.form['oxi Headache'] == 'on':
        feature4 = 0
    if request.form['nai Contact with COVID Patient'] == 'on':
        feature5 = 1
    elif request.form['oxi Contact with COVID Patient'] == 'on':
        feature5 = 0
    if request.form['nai Family working in Public Exposed Places'] == 'on':
        feature6 = 1
    elif request.form['oxi Family working in Public Exposed Places'] == 'on':
        feature6 = 0
    if request.form['nai Wearing Masks'] == 'on':
        feature7 = 1
    elif request.form['oxi Wearing Masks'] == 'on':
        feature8 = 0
    import numpy as np
    myfeatures = np.array([[feature1,feature2,feature3,feature4,feature5,feature6,feature7],
                ])        
    result2 = ml.result2(myfeatures)[0][1]
    return render_template('output.html', title='Output', result2 = result2)  
#request.form was displayed in output.html

app.run(host='0.0.0.0', port=81)
