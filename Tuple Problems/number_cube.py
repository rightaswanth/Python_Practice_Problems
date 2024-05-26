# Problem - 28
# Create a list of tuples from given list having number and its cube in each tuple

# Method - 1

number_cube = []

for i in range(10):
    t = (i, i**3)
    number_cube.append(t)

print(number_cube)

# Method - 2
# Using List Comprehension

number_cube = [(x, x**3) for x in range(10)]

print(number_cube)
