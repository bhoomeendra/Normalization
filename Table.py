import json

import Helper
from constants import LEFT, RIGHT


class Table:
    def __init__(self, attr, fds, normalForm):
        self.attr = attr
        self.fds = fds
        self.normalForm = normalForm;

    def show(self):
        print("Table Attributes : ", self.attr)
        self.displayFDs()

    def getAttr(self):
        return self.attr;

    def getFdsSet(self):
        return self.fds;

    def getNormalForm(self):
        return self.normalForm;

    def getFdById(self, index):
        left = self.fds[LEFT][index]
        right = self.fds[RIGHT][index]
        return [left, right]

    def setAttr(self, attr):
        self.attr = attr

    def setFds(self, fds):
        self.fds = fds

    def setNormalForm(self, normalForm):
        self.normalForm = normalForm

    def getNoOfFds(self):
        return len(self.fds[LEFT])

    def removeFdById(self,index):
        self.fds[LEFT].pop(index)
        self.fds[RIGHT].pop(index)
    def getNormalForm(self):
        return self.normalForm;

    def deleteFdById(self,index):
        del self.fds[LEFT][index]
        del self.fds[RIGHT][index]
    def displayFDs(self):
        print("Functional Dependency: ")
        for i in range(self.getNoOfFds()):
            print(self.fds[LEFT][i],"\t-------------->\t",self.fds[RIGHT][i])
    def deleteFdFor2NF(self,dfd):
        for index in range(len(self.fds[LEFT])):
            if(dfd[LEFT] == self.fds[LEFT][index]):
                if(dfd[RIGHT] == self.fds[RIGHT][index]):
                    self.deleteFdById(index)
                    newattr = set()
                    for i in range(self.getNoOfFds()):
                        newattr = newattr.union(self.fds[LEFT][i])
                        newattr = newattr.union(self.fds[RIGHT][i])
                    self.setAttr(newattr)
                    break

    def isEqual(self,table):
        if(self.getAttr() == table.getAttr()):
            if(self.getNoOfFds() == table.getNoOfFds()):
                for i in range(self.getNoOfFds()):
                   if(self.doesFdExit(table.getFdById(i))):
                        continue
                   else:
                       return False
            return True
        return False

    def doesFdExit(self,fd):
        for i in range(self.getNoOfFds()):
            if(fd[LEFT]== self.fds[LEFT][i] and fd[RIGHT]== self.fds[RIGHT][i]):
                return True
        return False

