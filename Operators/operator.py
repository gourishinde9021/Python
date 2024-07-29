my_list = [1, 2, 3, 4, 5]

# Identity Operator
a = my_list
b = [1, 3, 5, 7, 9]

is_same_object = a is my_list
is_not_same_object = a is not my_list

# Membership operators
element_in_list = 3 in my_list     # Returns Boolen value True/False
element_not_in_list = 6 not in my_list

print("a is my_list:", is_same_object)
print("b is not my_list:", is_not_same_object)
print("3 in my_list:", element_in_list)
print("6 not in my_list:", element_not_in_list)

# Assignment Operator

total = 10

total += 5    # Addition Assignment Operator
total -= 3    # Addition Subtraction Operator
total *= 2    # Addition Multiplication Operator
total /= 4    # Addition Division Operator

print("Final total:", total)