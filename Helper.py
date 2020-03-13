from copy import  deepcopy
import json
from Table import Table
from constants import RIGHT, LEFT, FD, ATTRIBUTE
from itertools import combinations

def Closer(table , attrSet):
    closer = set().union(attrSet)
    i=0
    while i<len(closer):
            for index in range(table.getNoOfFds()):
                fd = table.getFdById(index)
                if fd[LEFT].issubset(closer):
                   closer = closer.union(fd[RIGHT])
            i+=1
    return closer

def MinimalCover(table):
    # STEP 1
    newFds = [[],[]]
    #Decompstion in Single RHS attribute
    for index in range(table.getNoOfFds()):
        fd = table.getFdById(index)
        for attr in fd[RIGHT]:
            newFds[LEFT].append(fd[LEFT])
            newFds[RIGHT].append(set(attr))

    #STEP 2
    #Removing Useless Fds
    table.setFds(newFds)
    table.displayFDs()
    print("STEP 1" ,newFds)
    index = 0
    while index < table.getNoOfFds():
        fd = table.getFdById(index)
        #print(fd)
        tempTable = deepcopy(table)
        tempTable.removeFdById(index)
        closerWithFd =  Closer(table,fd[LEFT])
        #print("Closer With Fd",closerWithFd)
        closerWithoutFd = Closer(tempTable,fd[LEFT])
        #print("Closer Without Fd", closerWithoutFd)
        if(closerWithFd == closerWithoutFd):
         #   print("New FD SET :",tempTable.getFdsSet())
            table.setFds(tempTable.getFdsSet())
            continue
        index+=1
    newFds = table.getFdsSet()
    table.displayFDs()
    print("STEP 2: ", newFds)
    #STEP 3
    #Left Side reduction
    index = 0
    while(index<table.getNoOfFds()):
        fd = table.getFdById(index)
        closerWithAttr = Closer(table,fd[LEFT])
        newFdLeft = fd[LEFT]
        for attr in fd[LEFT]:
            if Closer(table,newFdLeft.difference(attr)) == closerWithAttr :
                newFdLeft = newFdLeft.difference(attr)
                newFds[LEFT][index] = newFdLeft
                table.setFds(newFds)
                print("Index",index ,"\nPrevious Left Fd:\t",fd[LEFT],"\n New FD Left:\t ",newFdLeft)
        index+=1
    table.displayFDs()
    print("STEP 3" , newFds)
    index = 0
    #STEP 4
    #Remove Redundent FDs
    while index <table.getNoOfFds():
        fd = table.getFdById(index)
        index_2 = index+1
        while(index_2<table.getNoOfFds()):
            fdLoop = table.getFdById(index_2)
            if FdEqualityChecker(fd,fdLoop):
                table.deleteFdById(index)
                break
            index_2 += 1
        index+=1
    #We can Recombine the FD's so optimize the algo
    table.displayFDs()
    print("STEP 4" , newFds)

    

def CandidateKey(table):

    essential = set(deepcopy(table.getAttr()))
    attrInLeft = set()
    attrInRight = set()
    for index in range(table.getNoOfFds()):
        fd = table.getFdById(index)
        attrInLeft=attrInLeft.union(fd[LEFT])
        attrInRight=attrInRight.union(fd[RIGHT])

    mayBeEssential = attrInLeft.intersection(attrInRight)
    essential = essential.difference(attrInRight)

    closerofEssential = Closer(table,essential)

    if closerofEssential == table.getAttr():
        return essential
    else:
        pcOfMayBeEssential = possibleCombination(mayBeEssential)
        setOfCandidateKeys = list()

        for possiblityOfSameSize in pcOfMayBeEssential:

            for singlePossiblity in possiblityOfSameSize:
                if Closer(table,essential.union(set(singlePossiblity))) == table.getAttr() :
                    if isSupersetOfSetin(setOfCandidateKeys,essential.union(set(singlePossiblity))) == False :
                        setOfCandidateKeys.append(essential.union(set(singlePossiblity)))

        return setOfCandidateKeys



def possibleCombination(attrs):
    pC = []
    for length in  range(1,len(attrs)+1 ):
        pC.append(list(combinations(attrs,length)))
    return pC;

def isSupersetOfSetin(setOfCandidateKeys , attrSet):

    if(len(setOfCandidateKeys) == 0):
        return False
    for cd in setOfCandidateKeys:
        if cd.issubset(attrSet):
            return True;
    return False

def FdEqualityChecker(fd1 ,fd2):

    if(fd1[LEFT] == fd2[LEFT] and  fd1[RIGHT] == fd2[RIGHT]):
        return True
    return False

def DataPaser(data):
    jsonData = json.loads(data)
    attr = set(jsonData[ATTRIBUTE])
    fds = jsonData[FD]
    left = list()
    right = list()

    for att in fds[LEFT]:
        left.append(set(att))
    for att in fds[RIGHT]:
        right.append(set(att))
    print(left,right)
    return Table(attr,[left,right],"1NF")
