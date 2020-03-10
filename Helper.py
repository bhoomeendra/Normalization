from copy import copy

from Table import Table
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
    #Decompstion in Single RHS attribute
    for index in range(table.getNoOfFds()):
        fd = table.getFdById(index)
        for attr in fd[RIGHT]:
            newFds[LEFT].append(fd[LEFT])
            newFds[RIGHT].append(attr)
    
    #STEP 2
    #Removing Useless Fds
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
    #Left Side reduction
    for index in range(table.getNoOfFds()):
        fd = table.getFdById(index)
        closerWithAttr = Closer(table,fd[LEFT])
        newFdLeft = fd[LEFT]
        for attr in fd[LEFT]:
            if Closer(table,newFdLeft.difference(attr)) == closerWithAttr :
                newFdLeft = newFdLeft.difference(attr)
    #STEP 4
    #Remove Redundent FDs
    for index in range(table.getNoOfFds()):
        fd = table.getFdById(index)
        index_2 = index+1
        while(index_2<table.getNoOfFds()):
            fdLoop = table.getFdById(index_2)
            if FdEqualityChecker(fd,fdLoop):
                table.deleteFdById(index)
                break
            index_2 += 1


    

def CandidateKey(table):

    essential = table.getAttr()
    attrInLeft = set()
    attrInRight = set()
    for index in range(table.getNoOfFds()):
        fd = table.getFdById(index)
        attrInLeft.add(fd[LEFT])
        attrInRight.add(fd[RIGHT])

    mayBeEssential = attrInLeft.intersection(attrInRight)
    essential = essential.difference(attrInRight)

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

def isSupersetOfSetin(setOfCandidateKeys , attrSet):

    for cd in setOfCandidateKeys:
        if cd.issubset(attrSet):
            return True;
    return False

def FdEqualityChecker(fd1 ,fd2):

    if(fd1[LEFT] == fd2[LEFT] and  fd2[RIGHT] == fd2[RIGHT]):
        return True
    return False

