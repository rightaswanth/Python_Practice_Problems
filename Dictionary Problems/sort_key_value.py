# Python | Sort Python Dictionaries by Key or Value

students = {'name': 'aswanth', 'age': 23, 'place': 'calicut', 'education': 'B tech'}

sorted_list = sorted(students)
sort_dict = {}

for key in sorted_list:
    i = 0
    value = students[key]
    sort_dict[key] = value 

print(sort_dict)



