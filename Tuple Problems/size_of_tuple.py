# Problem - 25
# Python program to Find the size of a Tuple

# Method - 1

scores = (23, 45, 67, 89, 34)
size = 0

for score in scores:
    size += 1

print(size)

# Method - 2

scores = (23, 45, 67, 89, 34)
size = len(scores)

print(size)
