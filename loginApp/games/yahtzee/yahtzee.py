'''
"Yahtzee"
Eshaan Tripathi
10/11/22
Play Yahtzee
'''

#import sys library
import sys

#define counts list
counts = []

#import random library
import random

#define rolls lists
rolls = []

#get random values and append to rolls list
for i in range(5):
    n = random.randint(1,6)
    rolls.append(n)

print(rolls)

#find how many of each element there is in a list
for i in range(6):
    list_count = rolls.count(i)
    counts.append(list_count)

#set the two and three variables as false
two = False
three = False

#loop through the counts list, find the frequency of elements, and then print the results based off of those 
for i in counts:
    if i == 3:
        three = True
    if i == 2:
        two = True
    if three == True and two == True:
        print("full house")
        sys.exit()
    for j in range(2,5):
        if i == j:
            print(f"{i} of a kind")
