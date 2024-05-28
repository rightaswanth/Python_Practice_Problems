# Python – Join Tuples if similar initial element

num_tup_one = (2, 3, 5, 7, 11)
num_tup_two = (1, 4, 6, 8, 9)

if num_tup_one[0] == num_tup_two[0]:
    new_number = list(num_tup_one) + list(num_tup_two)
    print(tuple(new_number))
else:
    print(f"The initial elements are not same")