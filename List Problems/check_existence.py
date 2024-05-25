# Problem - 4
# Python | Ways to check if element exists in list

# Method 1

states = ['TN', 'KA', 'AP', 'HR', 'MH']
element = input("Enter the element to find :")

for state in states:
    if state == element:
        flag = 1
        break
    else:
        continue

if flag == 1:
    print("The number is present in the list")
else:
    print("The number is not present in the list")


# Method - 2
    
states = ['TN', 'KA', 'AP', 'HR', 'MH']
element = input("Enter the element to find :")

if element in states:
    print("The element is present in the list :")
else:
    print("The Element is not in list")


# Method 3

states = ['TN', 'KA', 'AP', 'HR', 'MH']
element = input("Enter the element to find :")
value = states.count(element)

if value > 0:
    print("Print Element is present in the list")
else:
    print("Element is not present in the list")

