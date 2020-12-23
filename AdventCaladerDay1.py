"""
Specifically, they need you to find the two entries that sum to 2020
and then multiply those two numbers together. find the two entries
that sum to 2020 and then multiply those two numbers together.

data in file Adxvebt_day1_input

compare numbers pairs to find all combination that equals 2020
def a function to count the total number of lines in file for each
line exept itself check to see if = 2020 if true mutiiply paie and return

there is an edge case that you may check self and get answer.

"""


with open("Advent_day1_input.txt","r")as file:
    numList = file.read()
    #print(numList)

def advent():
    for line in numList.splitlines():
        print(line)
        for secNumber in numList.splitlines():
            check = int(line)+ int(secNumber) # add int line tp int(scnumber)
            if check == 2020:
                answer = int(line) * int(secNumber) # if == to 2020
                print (line , secNumber, answer)
                return

advent()
# answer = line * secnumber
        #answer = int(line)
        #print(line , answer)


"""
list comprehention
[x for x in list] this returns a list 
element we are rutning v element in the list 

"""
"""def advent2(): # 2 pointer method
    expensesList=[int(line) for line in numList.splitlines()]
    expensesList.sort()
    #print (expensesList)
    leftCounter = 0
    rightCounter= len(expensesList)-1
    while leftCounter < rightCounter :
        if (expensesList[leftCounter] + expensesList[rightCounter]) == 2020:

            return  expensesList[leftCounter] * expensesList[rightCounter]
        elif (expensesList[leftCounter] + expensesList[rightCounter]) > 2020:
            rightCounter -= 1
        else:
            leftCounter += 1
print (advent2())"""

"""from itertools import combinations
def expenseProd03(input_list, targetSum):
    for combos in combinations(input_list, 2):
        if sum(combos) == targetSum:
            print(combos)

            
"""
"""print()
def findTargetExpense(expenseArr, target): # using hash sets 

    # x + y = target
    # target -x = y

    selected = set()
    # expenseSet = set(expenseArr) #O(n)
    for num in expenseArr:
        if target - num in selected:
            return [num, target-num]
        selected.add(num) #O(1)

testExpense = [1975,1782, 1966,1395,1681,1236,1572,437,1583]
target = 2020

print(findTargetExpense(testExpense, target))

"""

