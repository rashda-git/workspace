from flask import Flask,request

import json
app = Flask(__name__)

@app.route("/calculate", methods =['POST'])
def calculate():
    request_data = request.get_json()
    value_1 = float(request_data['value_1'])
    value_2 = float(request_data['value_2'])
    
    resultMap = {
        '+' : value_1+value_2,
        '-' : value_1 - value_2,
        '*' : value_1 * value_2,
        '/' : value_1 / value_2
    }
  

    return json.dumps(resultMap)

@app.route("/sayhi")
def say():
    return "<p>say</p>"    

if __name__== '__main__':
    app.run()