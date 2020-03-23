from Helper import MinimalCover, CandidateKey
from constants import LEFT, RIGHT


def TwoNFDecompostion(table):#SET NORMAL FORM
    #Find Minimal Cover
    MinimalCover(table)
    cdKeys = CandidateKey(table)
    partialDepedency = [[],[]]

    #Finding Partial Depedency
    for cdKey in cdKeys:
        index = 0
        while index < table.getNoOfFds():
            fdLeft = table.getFdById(index)[LEFT]
            fdRight = table.getFdById(index)[RIGHT]

            if fdLeft != cdKey and fdLeft.issubset(cdKey):
                flag  = True
                for cdK in cdKey:
                    if fdRight.issubset(cdK):
                        flag = False
                        break
                if flag :
                    partialDepedency[LEFT].append(fdLeft)
                    partialDepedency[RIGHT].append(fdRight)
            index+=1
    #Merge PDs with same lhs
    newPd = [[],[]]
    for index in range(len(partialDepedency[LEFT])) :
