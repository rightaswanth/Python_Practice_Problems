# Problem - 6
# Python | Reversing a List

# Method - 1

names = ['Aks', 'Abi', 'Nj', 'Asw']
reversed_names = []

for name in range(len(names)-1,-1,-1):
    reversed_names.append(names[name])
    
print(reversed_names)

# Method - 2

names = ['Aks', 'Abi', 'Nj', 'Asw']
reversed_names = names[::-1]

print(reversed_names)

# Method - 3

names = ['Aks', 'Abi', 'Nj', 'Asw']
names.reverse()

print(names)




