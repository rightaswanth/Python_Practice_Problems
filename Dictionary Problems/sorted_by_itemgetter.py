# Problem - 24
# Ways to sort list of dictionaries by values in Python – Using itemgetter

from operator import itemgetter

person = [{'name':'abi', 'age':23, 'place':'calicut'}, {'name':'aks', 'age':25, 'place':'bangloor'}, {'name':'nj', 'age':24, 'place':'korea'}]

sorted_person = sorted(person,key=itemgetter('age'))

print(person)
print(sorted_person)