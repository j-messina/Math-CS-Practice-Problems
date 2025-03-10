import sys
sys.path.append('C:/Users/jwmes/Documents/GitHub/Math-CS-Practice-Problems')
from Algorithms.RemovePrintPath import *
RemovePrintPath()

list_of_vals_in_pence = [200,100,50,20,10,5,2,1]
list_desc = []
for x in list_of_vals_in_pence:
    list_desc.append([])
    for y in range(1,(int)(200/x)+1):
        list_desc[-1].append(y)
# print(list_desc)
        

"""
starting val: 200, then 100, then 50, then 10, then 5, then 2, 1

branches like a tree - can try self or lower value - always self first, then next highest value below self

keep a running sum of all the coins
keep a running counter of all found combinations
on arriving at 200, no more recursion, increment counter by one
on still below 200, recursive call for each coin option still available
have a starting list of all coins
having a running list of remaining available coins
update list as available coins shrinks
"""

all_coins = [200,100,50,20,10,5,2,1]

simple_version = [10,5,2,1]
simple_max = 10
true_max = 200

mycounter = 0

import copy

def simpleCoins(count = simple_max, remaining_coins = copy.deepcopy(simple_version)):
    global mycounter
    for x in remaining_coins:
        if x + count == simple_max:
            mycounter += 1
            templist = copy.deepcopy(remaining_coins)
            templist.pop(0)
        elif x + count > simple_max:
            templist = copy.deepcopy(remaining_coins)
            templist.pop(0)
        else: # x + count < simple_max
            templist = copy.deepcopy(remaining_coins)
            count += x

        if len(templist) > 0:
            simpleCoins(count, templist)


# simpleCoins(0)

def countPence(count = true_max, remaining_coins = copy.deepcopy(all_coins)):
    global mycounter
    for x in remaining_coins:
        if x + count == simple_max:
            mycounter += 1
            templist = copy.deepcopy(remaining_coins)
            templist.pop(0)
        elif x + count > simple_max:
            templist = copy.deepcopy(remaining_coins)
            templist.pop(0)
        else: # x + count < true_max
            templist = copy.deepcopy(remaining_coins)
            count += x
        if len(templist) > 0:
            countPence(count, templist)

countPence(0)

print("Results are: ", mycounter)