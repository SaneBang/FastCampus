 

def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num
    

print(factorial(10))


def multiple(num):
    if num <= 1:
        return num
    else:
        return num * multiple(num - 1)
    
print(multiple(10))
 

import random
from tkinter.tix import Tree
data = random.sample(range(100),10)

def sum_list(data):
    if len(data) == 1:
        return data[0]
    return data[0] + sum_list(data[1:])

print(sum_list(data))


def isPalindrome(data):
    if len(data) <= 1:
        return True
    if data[0] == data[-1]:
        return isPalindrome(data[1:-1])
    else:
        return False
    

def func(n):
    print(n)
    if n <= 1:
        return n
    
    if n % 2 == 1:
        return func(3 * n + 1)
    else:
        return int(func(n/2))
    
print(func(3))



# 1, 2, 4, 7, 13, 
# 1 + 2 + 4, 1 + 2 + 4 + 6, 1 + 2 + 4 + 6 + 8


def number1(data):
    array = [1, 2, 4]
    if data <= 3:
        return array[data-1]
    
    return number1(data-1) + number1(data-2) + number1(data-3)

print(number1(7))