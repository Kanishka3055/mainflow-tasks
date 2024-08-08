# Dictionary Operations
print("Dictionary Operations:")

# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", my_dict)

# Accessing values
print("Value for key 'a':", my_dict['a'])

# Adding/Updating key-value pairs
my_dict['d'] = 4
print("After adding 'd': 4:", my_dict)
my_dict['a'] = 5
print("After updating 'a': 5:", my_dict)

# Removing key-value pairs
my_dict.pop('a')
print("After popping key 'a':", my_dict)
del my_dict['b']
print("After deleting key 'b':", my_dict)

# Getting keys, values, and items
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# Checking for key existence
print("Is 'a' in dictionary?", 'a' in my_dict)
print("Is 'c' in dictionary?", 'c' in my_dict)

# Dictionary comprehensions
squares = {x: x**2 for x in range(5)}
print("Dictionary comprehension (squares):", squares)

# Merging dictionaries (Python 3.9+)
merged_dict = {**my_dict, **{'e': 5, 'f': 6}}
print("Merged dictionary:", merged_dict)