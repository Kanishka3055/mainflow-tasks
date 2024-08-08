# Tuple Operations
print("Tuple Operations:")

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing
print("Slice [1:3]:", my_tuple[1:3])
print("Slice [:3]:", my_tuple[:3])
print("Slice [3:]:", my_tuple[3:])

# Tuple concatenation
new_tuple = my_tuple + (6, 7)
print("After concatenation with (6, 7):", new_tuple)

# Tuple multiplication
repeated_tuple = my_tuple * 2
print("After multiplication by 2:", repeated_tuple)

# Unpacking tuples
a, b, c, d, e = my_tuple
print(f"Unpacked values: a={a}, b={b}, c={c}, d={d}, e={e}")

# Tuple comprehensions (Generator)
gen = (x**2 for x in my_tuple)
print("Tuple comprehension (generator):", tuple(gen))