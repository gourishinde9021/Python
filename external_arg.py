# Read external variables passed to python script by importing sys package

import sys

def add1(num1, num2):
    sum1 = num1 + num2
    return sum1

def substraction1(num1, num2):
    sub = num1 - num2
    return sub

def multiplication1(num1, num2):
    mult = num1 * num2
    return mult

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add1":
    output = add1(num1, num2)
    print(output)

