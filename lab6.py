

"""Structured English
To, start we will generate a random integer between one and twenty, and
based on the result of the random number, we check to see if it falls under a certain range.
If the number is greater than 15, then the result will be "Cherries"
otherwise if the number is greater than 10 the result will be "Orange"
otherwise if the number is greater than 5 the result will be "Melon
otherwise if the number is greater than 1 the result will be "Bell"
otherwise the result will be "Bar"
We interate over useing a loop three times and print the results to the user. Ex "Cherries, Orange, Melon"

"""
"""Psudocode
import random
num = generate random number

If number is greater than 15
    then the result will be "Cherries"
otherwise if the number is greater than 10
     then result will be "Orange"
otherwise if the number is greater then 5
     the result will be "Melon
otherwise if the number is greater then 1 
    the result will be "Bell"
otherwise 
    the result will be "Bar"

loop three times
    print the output to the user
"""

import random

def main():
    for i in range(0,3):
        print ("i---->", i)
        spin()
def spin():
    rand = random.randint(1,20)

    output = ""
    if (rand > 15):
        output = "Cherries"
    elif (rand > 10):
        output = "Orange"
    elif (rand > 5):
        output = "Melon"
    elif (rand > 1):
        output = "Bell"
    else:
        output = "Bar"

    print(output, end="")

main()