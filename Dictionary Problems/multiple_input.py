# Python dictionary with keys having multiple inputs

numbers = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

numbers_dict = {}
i = 0

for num in numbers:
    numbers_dict[num] = i
    i += 1

print(numbers_dict)