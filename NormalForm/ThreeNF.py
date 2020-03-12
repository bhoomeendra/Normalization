from NormalForm.TwoNF import TwoNFDecompostion


def ThreeNFDecompostion(table):

    twoNFTables = TwoNFDecompostion(table)
    threeNFtable = list()
    for twoNFTable in twoNFTables:
        threeNFtable+=ThreeNFConversion(table)

    return threeNFtable

def ThreeNFConversion(table):#SET NORMAL FORM
    pass