from Helper import MinimalCover, TansistiveDependency
from NormalForm.TwoNF import  decompose2NF
from Table import Table
from constants import LEFT, RIGHT


def ThreeNFDecompostion(table):

    twoNFTables = decompose2NF(table)
    threeNFtable = list()
    for twoNFTable in twoNFTables:
        threeNFtable+=ThreeNFConversion(Table(twoNFTable.getAttr(),twoNFTable.getFdsSet(),twoNFTable.getNormalForm(),twoNFTable.getPid(),twoNFTable.getId()))
    return [twoNFTables,threeNFtable]

def ThreeNFConversion(table):
    MinimalCover(table)
    transitiveDependency = TansistiveDependency(table)
    table.show()
    print("Transistive Dependency: ")
    print(transitiveDependency)
    if(len(transitiveDependency[LEFT]) == 0):
        table.setNormalForm("3NF")
        return [table]
    threeNFtables = list()

    for index in range(len(transitiveDependency[LEFT])):
        tfd = [transitiveDependency[LEFT][index],transitiveDependency[RIGHT][index]]
        attr = tfd[LEFT].union(tfd[RIGHT])
        table.deleteFdForNormalization(tfd)
        threeNFtables.append(Table(attr,[[tfd[LEFT]],[tfd[RIGHT]]],"3NF",table.getId(),0))

    table.setNormalForm("3NF")
    threeNFtables.append(Table(table.getAttr(),table.getFdsSet(),table.getNormalForm(),table.getId(),0))
    return threeNFtables
