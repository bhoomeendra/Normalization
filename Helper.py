from copy import copy

from Table import Table
from constants import RIGHT, LEFT
from itertools import combinations

def Closer(table , attrSet):
    closer = set().union(attrSet)

    for i in range(len(closer)):
            for index in range(table.getNoOfFds()):
                fd = table.getFdById(index)
                fdLeft = fd[LEFT]
                fdRight = fd[RIGHT]
                if fdLeft.issubset(closer):
                   closer = closer.union(fdRight)

    return closer

def MinimalCover(table):
    # STEP 1
    newFds = [[],[]]
    for index in range(table.getNoOfFds()):
        fd = table.getFdById(index)
        for attr in fd[RIGHT]:
            newFds[LEFT].append(fd[LEFT])
            newFds[RIGHT].append(attr)
    #STEP 2
    table.setFds(newFds)
    index = 0
    while index < table.getNoOfFds():
        fd = table.getFdById(index)
        tempTable = Table(table.getAttr(), table.getFdsSet(), table.getNormalForm())
        tempTable.removeFdById(index)
        closerWithFd =  Closer(table,fd[LEFT])
        closerWithoutFd = Closer(tempTable,fd[LEFT])

        if(closerWithFd.equals(closerWithoutFd)):
            table = tempTable
            continue
        index+=1

    #STEP 3



def CandidateKey(table):
    pass;

def possibleCombination(attrs):
    pC = []
    for length in  range(1,len(attrs)+1 ):
        pC.append(list(combinations(attrs,length)))
    return pC;




