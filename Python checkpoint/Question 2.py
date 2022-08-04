# Write a program that can compute the factorial of a given number.
# (The factorial of n is the product of all positive integers less than or equal to n.)
# For example: For factorial(5)= 5 x 4 x 3 x 2 x 1 the result is 120 (i.e. factorial (0)=1).

def factorial(num):
    if num == 0:
        return 1
    else:
        return (num * factorial(num-1))

num = factorial(4)
print(num)