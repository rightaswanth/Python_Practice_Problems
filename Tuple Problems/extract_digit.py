# Python – Extract digits from Tuple list

tuple_list = ([1,2], ["i am", 23], ['hello','world'])
digits_list = []

for t in tuple_list:
    for dig in t:
        if type(dig) == int:
            digits_list.append(dig)

print(digits_list)



