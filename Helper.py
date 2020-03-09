from constants import RIGHT, LEFT
from itertools import combinations

def Closer(table , attrSet):
    closer = set().union(attrSet)

    for i in range(len(closer)):
            for index in range(table.getNoOfFds()):
                fd = table.getFdById(index)
                if fd[LEFT].issubset(closer):
                   closer.add(fd[RIGHT])

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

    #STEP 3




def CandidateKey(table):

    essential = table.getAttr()
    mayBeEssential = set()
    notEssential = set()#will not be used

    attrInLeft = set()
    attrInRight = set()
    for index in range(table.getNoOfFds()):
        fd = table.getFdById(index)
        attrInLeft.add(fd[LEFT])
        attrInRight.add(fd[RIGHT])

    mayBeEssential = attrInLeft.intersection(attrInRight)
    essential = essential.difference(attrInRight)
    notEssential= attrInRight.difference(attrInLeft)

    closerofEssential = Closer(table,essential)

    if closerofEssential == table.getAttr():
        return essential
    else:
        pcOfMayBeEssential = possibleCombination(mayBeEssential)
        setOfCandidateKeys = list()

        for possiblity in pcOfMayBeEssential:

            if Closer(table,essential.union(possiblity)) == table.getAttr() :
                if isSupersetOfSetin(setOfCandidateKeys,essential.union(possiblity)) == False :
                    setOfCandidateKeys.append(essential.union(possiblity))

        return setOfCandidateKeys



def possibleCombination(attrs):
    pC = []
    for length in  range(1,len(attrs)+1 ):
        pC.append(list(combinations(attrs,length)))
    return pC;

def isSupersetOfSetin(setOfCandidateKeys , attrSet ):

    for cd in setOfCandidateKeys:
        if cd.issubset(attrSet):
            return True;
    return False



