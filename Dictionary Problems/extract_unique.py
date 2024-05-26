# Problem - 21
# Python – Extract Unique values dictionary values

# Method - 1

person = {'name':'abi', 'place':'calicut', 'address':'calicut', 'age':23, 'year':23, 'education':'b tech'}
value_list = []
unique_values = []

for value in person.values():
    value_list.append(value)

for value in value_list:
    if value_list.count(value) < 2:
        unique_values.append(value)

print(unique_values)


