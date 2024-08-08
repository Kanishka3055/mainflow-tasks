# List Operations
print("List Operations:")

# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Accessing elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Slicing
print("Slice [1:3]:", my_list[1:3])
print("Slice [:3]:", my_list[:3])
print("Slice [3:]:", my_list[3:])

# Appending elements
my_list.append(6)
print("After appending 6:", my_list)

# Inserting elements
my_list.insert(2, 10)
print("After inserting 10 at index 2:", my_list)

# Removing elements
my_list.remove(10)
print("After removing 10:", my_list)

# Popping elements
print("Popped element:", my_list.pop())
print("After popping the last element:", my_list)
print("Popped element at index 1:", my_list.pop(1))
print("After popping element at index 1:", my_list)

# Extending a list
my_list.extend([5, 6])
print("After extending with [5, 6]:", my_list)

# Sorting a list
my_list.sort()
print("After sorting:", my_list)
my_list.sort(reverse=True)
print("After sorting in reverse:", my_list)

# Reversing a list
my_list.reverse()
print("After reversing:", my_list)

# List comprehensions
squares = [x**2 for x in my_list]
print("List of squares using list comprehensions:", squares)