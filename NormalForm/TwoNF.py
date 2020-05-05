from Helper import MinimalCover, CandidateKey, Closer, PartialDependency
from Table import Table
from constants import LEFT, RIGHT


def TwoNFDecompostion(table):#SET NORMAL FORM
    #Find Minimal Cover
    if(len(table.getAttr()) == 0):
        return []
    MinimalCover(table)
    print("Decomposing the Following Table")
    table.show()
    cdKeys = CandidateKey(table)

    newPd = PartialDependency(table,cdKeys)

    #Each PD will have a table(Table and relation are synonyms)
    tables = []
    if(len(newPd[LEFT]) == 0):#No Partial Dependency found
        table.setNormalForm("2NF")
        tables.append(table)
        return tables
    # Recursively check for Partial dependency
    for tableIndex in range(len(newPd[LEFT])):
        attr = newPd[LEFT][tableIndex].union(newPd[RIGHT][tableIndex])
        dtable = Closer(table,attr,True)#will also return fds Used in the right part
        for fdi in range(len(dtable[RIGHT][LEFT])):
            table.deleteFdForNormalization([dtable[RIGHT][LEFT][fdi],dtable[RIGHT][RIGHT][fdi]])
        dtablesPd = TwoNFDecompostion(Table(dtable[LEFT],dtable[RIGHT],"1NF"))
        tables.extend(dtablesPd)
        dtablesNotPd = TwoNFDecompostion(Table(table.getAttr(),table.getFdsSet(),"1NF"))
        tables.extend(dtablesNotPd)

    cdKeyUnion = set()
    for cdKey in cdKeys:
        cdKeyUnion = cdKeyUnion.union(cdKey)
    tables.append(Table(cdKeyUnion,[[],[]],"2NF"))
    #Remove Redundent Tables
    finaltable = list()
    for Dtable in tables:
        flag = False
        for FDtable in finaltable:
            if FDtable.isEqual(Dtable):
                flag = True
                break
        if(not flag):
            finaltable.append(Dtable)


    for Dtable in finaltable:
        Dtable.show()
#   Merge Empty relations
    return finaltable

def decompose2NF(table):
    twoNFTables  = TwoNFDecompostion(table)
    emptyTables = list()
    nonEmptyTables = list()
    for table in twoNFTables:
        if(table.getNoOfFds() == 0):
            emptyTables.append([table,table.getAttr()])
        else:
            nonEmptyTables.append([table,CandidateKey(table)])
    #Merge Empty Tables
    index = list()
    for i in range(len(emptyTables)):
        for j in range(len(emptyTables)):
            if( i != j):
                if(emptyTables[i][RIGHT].issubset(emptyTables[j][RIGHT])):
                  index.append(i)# This are the empty realtion that are not needed because they are already present
                  break
    newEmptyTables = list()
    for i in range(len(emptyTables)):
        if( i not in index):
            newEmptyTables.append(emptyTables[i])
    #Empty Tables that are  already present within some nonempty table
    index.clear()
    for eptyTable in newEmptyTables:
        for nonEptyTable in nonEmptyTables:
            if(eptyTable[RIGHT].issubset(nonEptyTable[RIGHT][0])):
                index.append(eptyTable)
    emptyTables.clear()
    for newETable in newEmptyTables:
        if(newETable not in index):
            emptyTables.append(newETable[LEFT])
    alltables = list()
    alltables.extend(emptyTables)
    for getTable in nonEmptyTables:
        alltables.append(getTable[LEFT])
    return alltables





