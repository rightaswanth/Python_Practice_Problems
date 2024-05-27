# Python – All pair combinations of 2 tuples

odd_tuple = (1, 3, 5, 7, 9)
even_tuple = (2, 4, 6, 8, 10)

combination_list = []

for odd, even in zip(odd_tuple, even_tuple):
    t = (odd, even)
    combination_list.append(t)

print(combination_list)

