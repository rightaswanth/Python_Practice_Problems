# Problem - 5
# Different ways to clear a list in Python

# Method - 1

fruits = ['apple', 'orange', 'mango', 'jerry']
fruits.clear()

print(fruits)

# Method - 2

fruits = ['apple', 'orange', 'mango', 'jerry']

del fruits[:]

print(fruits)

# Method - 3
fruits = ['apple', 'orange', 'mango', 'jerry']

for i in range(len(fruits)-1):
  fruits.pop(i)
  
print(fruits)
  







