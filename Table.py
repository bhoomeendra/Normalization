class Table:
    def __init__(self, attr, fds,normalForm):
        self.attr = attr
        self.fds = fds
        self.normalForm = normalForm;
    def show(self):
        print(" Table Attributes : ", self.attr)
        print("Table Funtional Dependencies ", self.fds)

    def getAttr(self):
        return self.attr;

    def getFdsSet(self):
        return self.fds;

    def getNormalForm(self):
        return self.normalForm;

    def getFdById(self, index):
        left = self.fds[0][index]
        right = self.fds[1][index]
        return [left, right]

    def setAttr(self,attr):
        self.attr = attr

    def setFds(self, fds):
        self.fds = fds

    def setNormalForm(self,normalForm):
        self.normalForm =normalForm

    def getNoOfFds(self):
        return len(self.fds[0])