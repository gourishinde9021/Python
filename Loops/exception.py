import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

try:
    div = num1 / num2
    print(div)
except ZeroDivisionError:
    print("Please do not provide 0 as input.")
