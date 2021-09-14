from flask import Flask
from flask import render_template
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
    return render_template('output.html', title='Output', percentage=percentage, result=result)  


app.run(host='0.0.0.0', port=81)
