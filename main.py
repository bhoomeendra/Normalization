import json

from Table import Table
from Helper import possibleCombination, Closer, MinimalCover, DataPaser
from flask import Flask,request,jsonify
from flask_cors import CORS
import  jsonpickle
from constants import FD, ATTRIBUTE

app = Flask(__name__)
cors = CORS(app)

@app.route('/Decompose',methods=['POST'])
def DecomposeTable():
    table = DataPaser(request.data.decode("utf-8"))

    return jsonpickle.encode(table) #Make a Json Parser Function that will loop over all the table

if(__name__ == "__main__"):
    app.run(debug=False)


















attr = {"A", "B", "C", "D", "E"}
fds = [[{"A", "B"}, {"D"}],[{"C"}, {"E"}]]

table = Table(attr, fds , "1NF");

print(MinimalCover(table))

