from Table import Table
from Helper import possibleCombination, Closer

attr = {"A", "B", "C", "D", "E"}
fds = [[{"A", "B"}, {"D"}],[{"C"}, {"E"}]]

table = Table(attr, fds , "1NF");

print(Closer(table, {"A","B"}))
#print(possibleCombination(attr))

