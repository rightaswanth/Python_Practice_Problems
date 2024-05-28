# Sort a list of tuples by second Item

squre_pairs = [(2, 4), (4, 16), (3, 9), (6, 36), (5, 25)]

sorted_squres = sorted(squre_pairs, key = lambda x: x[1])

print(sorted_squres)