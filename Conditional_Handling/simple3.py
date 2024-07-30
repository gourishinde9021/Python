import sys

type = sys.argv[1]

if type == "t2.micro":
    print("Ok, We will create an instance for you.")
elif type == "t2.medium":
    print("This will charge you 2 Dollar a day")
elif type == "t2.xlarge":
    print("This will charge you 10 Dollar a day")
else:
    print("Not valid instance type.")