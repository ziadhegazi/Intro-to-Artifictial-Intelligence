# Question: Write a program that calculates and prints the value according
# to the given formula: Q= Square root of [(2 * C * D)/H]
# The following are the fixed values of C and H: C is 50. H is 30.
# D is the variable whose values should be input into your program
# in a comma-separated sequence. (That means D contains more than value)
# Example: Let's assume the following comma-separated input sequence is given
# to the program: 100,150,180 The output of the program should be 18,22,24
# To further explain this, we will obtain a result for each value of D:
# Q1= Square root of [(2 * C * 100)/H] =18, Q2= Square root of [(2 * C * 150)/H]
# = 22 and Q3 = Square root of [(2 * C * 180)/H]  = 24

import numpy as np

def equation(D):
    list = []
    for i in range(len(D)):
        C = 50
        H = 30
        Q = round(np.sqrt((2 * C * int(D[i]))/H))
        list.append(Q)
    return list

text = input("Enter values here: ")
list = text.split(sep =("," or ", "))
num = equation(list)
print(text)

print(type(num))
print(num)