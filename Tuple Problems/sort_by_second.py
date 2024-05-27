# Sort a list of tuples by second Item

number_tuple = [(2,4), (6,7), (4,6), (8,10), (8,9)]

sorted_list = sorted(number_tuple, key = lambda x : x[1])
print(sorted_list)