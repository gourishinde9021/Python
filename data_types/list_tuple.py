name = ["a", "b", "c", "d", "e"]  # List
name_tuple = ("a", "b", "c", "d", "e")   # Tuple is immutable

print("List: ", name)
print("Tuple", name_tuple)

name.append("f")     # List is mutable
print("Updated List: ", name)

name.remove("a")
print("Updated List: ", name)

# List indexing

print(name[0])  
print(name[1])

print("Lenght of list name is", len(name))

my_list = [1, 2, 3, 'apple', 'banana']

# Slicing of list
my_new_list = my_list[3:5]
print(my_new_list)

print("print last two items of my_list: ", my_list[-1:-3:-1])

print("Reverse my_list: ", my_list[::-1])


# Sorting

numbers = [1, 3, 4, 6, 8, 2, 5, 7]
#numbers.sort()
#print("Sorted list: ", numbers)
print("Sorted list: ", sorted(numbers))

# Concatination

name = ["a", "b", "c", "d", "e"]
print(name[0] + "--" + name[3] + name[4])


