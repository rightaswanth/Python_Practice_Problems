# Python | Sort Python Dictionaries by Key or Value

students = {'name': 'aswanth', 'age': 23, 'place': 'calicut', 'education': 'B tech'}

sorted_list = sorted(students)
sort_dict = {}

# Sorted By keys

for key in sorted_list:
    value = students[key]
    sort_dict[key] = value 

print(sort_dict)

# Sorted By Values

students = {'name': 123, 'age': 23, 'place': 11, 'education': 12}

values_list = sorted([x for x in students.values()])
sort_dict = {}

for value in values_list:
    for key in students.keys():
        if students[key] == value:
            sort_dict[key] = value

print(sort_dict)




