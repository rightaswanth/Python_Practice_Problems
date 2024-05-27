# Problem - 18
# Find length of a string in python (4 ways)

# Method - 1

# fruit = "apple"
# length = len(fruit)

# print("The length of the string is :",length)

# Method - 2

# fruit = "apple"
# length = 0

# for f in fruit:
#     length += 1

# Method - 3
    
fruit = "apple"
length = 0
i = 0

while i <= length:
    try:
        fruit[i]
        i += 1
        length = i
    except IndexError:
        length = length + 1
        print("The length of the string is ",length + 1)

    
 


