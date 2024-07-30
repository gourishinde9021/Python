# For loop

fruits = ["apple", "banana", "grapes", "chikoo"]
for fruit in fruits:
    print(fruit)

for i in range(10):
    print(i)


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "voilet"]
for color in colors:
    print(color)

# while loop

count = 0
while count < 5:
    print(count)
    count += 1

log_file = [
    "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed"
]

for line in log_file:
    if "ERROR" in line:
        print(line)

# Break statement

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print(number)

# continue statement
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    print(number)