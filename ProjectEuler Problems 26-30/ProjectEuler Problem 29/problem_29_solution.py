import sys
sys.path.append('/Users/johnmessina/Documents/GitHub/Math-CS-Practice-Problems/Math-CS-Practice-Problems/')
from Algorithms.RemovePrintPath import *
RemovePrintPath()

myset = set()
for a in range(2, 101):
    for b in range(2, 101):
        myset.add(a**b)

print(len(myset))