import pandas as pd
from flask import Flask, jsonify, request, send_file
import mainModel


# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)
    print("test1")
    print(data)
    filename = mainModel.percentageOfMoneyGraph(data)

    return send_file(filename, mimetype='image/jpeg')

    
    

if __name__ == '__main__':
    app.run(port = 5000, debug=True)