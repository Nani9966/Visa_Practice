from flask import Flask
from visa.logger import logging 
from visa.exception import CustomException

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    try:
        raise Exception("We are testing our Custom Exceptio file")
    except Exception as e:
        return "hello worlds"
    

if __name__=="__main__":
    app.run(debug=True)