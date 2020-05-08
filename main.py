import json

from NormalForm.BCNF import BCNFDecompostion
from NormalForm.ThreeNF import ThreeNFDecompostion
from NormalForm.TwoNF import  decompose2NF

from Helper import  DataPaser
from flask import Flask,request,jsonify
from flask_cors import CORS
import  jsonpickle

#attr = {"A", "B", "C", "D", "E"}
#fds = [[{"A", "B"}, {"D"}],[{"C"}, {"E"}]]

app = Flask(__name__)
cors = CORS(app)

@app.route('/Decompose',methods=['POST'])
def DecomposeTable():
    table = DataPaser(request.data.decode("utf-8"))
    Dtablesin3NF = BCNFDecompostion(table)
    for table in Dtablesin3NF:
        table.show()
    return jsonpickle.encode(table) #Make a Json Parser Function that will loop over all the table and paser them as json

if(__name__ == "__main__"):
    app.run(debug=False)




