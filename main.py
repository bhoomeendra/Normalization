import ast
import json

from NormalForm.BCNF import BCNFDecompostion
from NormalForm.ThreeNF import ThreeNFDecompostion
from NormalForm.TwoNF import  decompose2NF

from Helper import DataPaser, jsonParser
from flask import Flask,request,jsonify
from flask_cors import CORS
import  jsonpickle

#attr = {"A", "B", "C", "D", "E"}
#fds = [[{"A", "B"}, {"D"}],[{"C"}, {"E"}]]
from Table import Table

app = Flask(__name__)
cors = CORS(app)

@app.route('/Decompose',methods=['POST'])
def DecomposeTable():
    table = DataPaser(request.data.decode("utf-8"))
    Dtablesin2NF = decompose2NF(Table(table.getAttr(),table.getFdsSet(),"1NF",-1,0))
    Dtablesin3NF = ThreeNFDecompostion(Table(table.getAttr(),table.getFdsSet(),"1NF",-1,0))
    DtablesinBcNF = BCNFDecompostion(Table(table.getAttr(),table.getFdsSet(),"1NF",-1,0))
    DecomposeTables = DtablesinBcNF


    #Will need to Write a custom parser
    response  = jsonParser(DecomposeTables)
    as_dicts = [ast.literal_eval(x) for x in response]
    as_json = json.dumps(as_dicts)
    return as_json

if(__name__ == "__main__"):
    app.run(debug=False)




