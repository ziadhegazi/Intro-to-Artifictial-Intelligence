# Write a program that will find all numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a list.

def findAll():
    arr = []
    for i in range(2000, 3200, 1):
        if (i%7 == 0) and (i%5 != 0):
            arr.append(i)
    return arr

list = findAll()
print(list)
