# Problem - 25
# Ways to sort list of dictionaries by values in Python – Using lambda function

# Method - 1

person = [{'name':'abi', 'age':23, 'place':'calicut'}, {'name':'aks', 'age':25, 'place':'bangloor'}, {'name':'nj', 'age':24, 'place':'korea'}]

sorted_person = sorted(person,key=lambda val : val['place'])

print(person)
print(sorted_person)