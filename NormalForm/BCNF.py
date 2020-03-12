from NormalForm.ThreeNF import ThreeNFDecompostion


def BCNFDecompostion(table):#SET NORMAL FORM

    threeNFTables = ThreeNFDecompostion(table)
    BCNFTables = list()
    for threeNFTable in threeNFTables:
        BCNFTables += BCNFConversion(threeNFTable)

    return BCNFTables

def BCNFConversion(table):
    pass

