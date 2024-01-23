import sys
sys.path.append('/Users/johnmessina/Documents/GitHub/Math-CS-Practice-Problems/Math-CS-Practice-Problems/')
from Algorithms.RemovePrintPath import *
RemovePrintPath()

list_of_vals_in_pence = [200,100,50,20,10,5,2,1]
list_desc = []
for x in list_of_vals_in_pence:
    list_desc.append([])
    for y in range(1,(int)(200/x)+1):
        list_desc[-1].append(y)
# print(list_desc)
        
