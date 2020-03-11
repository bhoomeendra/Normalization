from Table import Table
from Helper import possibleCombination, Closer, MinimalCover
from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/Decompose',methods=['POST'])
def DecomposeTable():
    attr = request.json['attribute']
    fds  = request.json['fd']
    print("Attributes: ",attr)
    print("Functional Dependency: ",fds)
    #Pasre this into fd list of list of set's
    return jsonify(fds)

if(__name__ == "__main__"):
    app.run(debug=True)


















attr = {"A", "B", "C", "D", "E"}
fds = [[{"A", "B"}, {"D"}],[{"C"}, {"E"}]]

table = Table(attr, fds , "1NF");

print(MinimalCover(table))

