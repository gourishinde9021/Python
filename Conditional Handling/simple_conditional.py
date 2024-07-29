x = int(input("Enter a number: "))

if x > 15:
    print(f"{x} is greater than 15")
elif x > 5:
    print(f"{x} is greater than 5 but not greater than 15")
else:
    print(f"{x} is not greater than 5")