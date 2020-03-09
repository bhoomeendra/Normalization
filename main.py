from Table import Table
from Helper import possibleCombination, Closer, MinimalCover

attr = {"A", "B", "C", "D", "E"}
fds = [[{"A", "B"}, {"D"}],[{"C"}, {"E"}]]

table = Table(attr, fds , "1NF");

print(MinimalCover(table))

