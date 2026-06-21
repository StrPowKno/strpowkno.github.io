from flask import Flask
from flask import make_response
from flask import render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

#@app.errorhandler(404)
#def not_found(error):
#    return render_template('error.html'), 404