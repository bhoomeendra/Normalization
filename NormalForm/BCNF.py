from Helper import MinimalCover, DependencyForBcnf
from NormalForm.ThreeNF import ThreeNFDecompostion
from Table import Table
from constants import LEFT, RIGHT


def BCNFDecompostion(table):#SET NORMAL FORM

    twoAndthreeNFTables = ThreeNFDecompostion(table)
    threeNFTables = twoAndthreeNFTables[1]
    twoNFTables =  twoAndthreeNFTables[0]
    BCNFTables = list()
    for threeNFTable in threeNFTables:
        BCNFTables += BCNFConversion(Table(threeNFTable.getAttr(),threeNFTable.getFdsSet(),threeNFTable.getNormalForm(),threeNFTable.getPid(),threeNFTable.getId()))

    AllTables = list()
    AllTables = threeNFTables+twoNFTables+BCNFTables

    return AllTables

def BCNFConversion(table):
    MinimalCover(table)
    pD = DependencyForBcnf(table)

    if(len(pD[LEFT]) == 0):
        table.setNormalForm("BCNF")
        return [table]
    bcnfTable = list()
    for i in range(len(pD[LEFT])):
        pdl = pD[LEFT][i]
        pdr = pD[RIGHT][i]
        attr = pdl.union(pdr)
        table.deleteForBcnf([pdl,pdr])
        nTable = Table(attr,[[pdl],[pdr]],"3NF",table.getId(),0)
        bcnfTable.extend(BCNFConversion(table))
        bcnfTable.extend(BCNFConversion(nTable))

    return bcnfTable

