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
        if(len(fd[RIGHT]) > 1):
            for attr in fd[RIGHT]:
                newFds[LEFT].append(fd[LEFT])
                newFds[RIGHT].append(attr)
    #STEP 2





def CandidateKey(table):
    pass;

def possibleCombination(attrs):
    pC = []
    for length in  range(1,len(attrs)+1 ):
        pC.append(list(combinations(attrs,length)))
    return pC;




