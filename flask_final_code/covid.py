from flask import Flask
from flask import render_template
#?
from app import app

#?
app = Flask(__name__)

@app.route("/")
def data_input():
#    return "<p>Hello, World!</p>"
#    return render_template('index.html', title='Home', user=user)  
    return render_template('index.html', title='Home')  

@app.route("/output")
def data_output():
    return render_template('output.html', title='Output')  


app.run(host='0.0.0.0', port=81)
